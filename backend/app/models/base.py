from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from typing import Type, List, TypeVar, Optional

from app.database import Base
from app.queries import SoftDeleteQuery

T = TypeVar("T", bound="BaseModel")


class BaseModel(Base):
    __abstract__ = True
    query_class: Type[SoftDeleteQuery] = SoftDeleteQuery

    async def save(self, session: AsyncSession) -> "BaseModel":
        try:
            session.add(self)
            await session.commit()
            return self
        except SQLAlchemyError:
            await session.rollback()
            raise

    @classmethod
    async def get_or_raise(cls: Type[T], session: AsyncSession, id: int) -> T:
        result = await session.get(cls, id)
        if not result:
            raise ValueError(f"{cls.__name__} with id {id} not found")
        return result

    @classmethod
    async def get_from_id(cls: Type[T], session: AsyncSession, id: int) -> Optional[T]:
        return await session.get(cls, id)

    @classmethod
    async def get_all(cls: Type[T], session: AsyncSession) -> List[T]:
        result = await session.execute(select(cls))
        return list(result.scalars().all())

    @classmethod
    async def find_one_by(cls: Type[T], session: AsyncSession, **kwargs) -> Optional[T]:
        stmt = select(cls).filter_by(**kwargs).limit(1)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def find_one_by_or_raise(cls: Type[T], session: AsyncSession, **kwargs) -> T:
        instance = await cls.find_one_by(session, **kwargs)
        if not instance:
            raise ValueError(f"{cls.__name__} not found for {kwargs}")
        return instance

    @classmethod
    async def filter_by(cls: Type[T], session: AsyncSession, **kwargs) -> List[T]:
        stmt = select(cls).filter_by(**kwargs)
        result = await session.execute(stmt)
        return list(result.scalars().all())

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

    async def soft_delete(self, session: AsyncSession) -> None:
        if hasattr(self, "deleted_at"):
            self.deleted_at = self.set_utc_now()
            await self.save(session)

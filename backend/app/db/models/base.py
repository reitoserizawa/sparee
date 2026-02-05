from typing import Optional, Sequence, Type, TypeVar, Any
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.sql import Select
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import Base
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

T = TypeVar("T", bound="BaseModel")


class BaseModel(Base):
    __abstract__ = True

    async def save(self: "BaseModel", session: AsyncSession) -> "BaseModel":
        try:
            session.add(self)
            await session.commit()
            return self
        except SQLAlchemyError:
            await session.rollback()
            raise

    async def soft_delete(self: "BaseModel", session: AsyncSession) -> None:
        if hasattr(self, "deleted_at"):
            self.deleted_at = datetime.now(timezone.utc)
            await self.save(session)

    @classmethod
    def _soft_delete_filter(cls: Type[T], stmt: Select) -> Select:
        if hasattr(cls, "deleted_at"):
            stmt = stmt.where(cls.deleted_at.is_(None))
        return stmt

    @classmethod
    async def get_or_raise(
        cls: Type[T],
        session: AsyncSession,
        id: int,
        include_deleted: bool = False
    ) -> T:
        """
        Get an instance by ID, raise if not found.
        If include_deleted is False, soft-deleted rows (deleted_at != None) are ignored.
        """
        stmt = select(cls).where(cls.id == id)
        if not include_deleted and hasattr(cls, "deleted_at"):
            stmt = cls._soft_delete_filter(stmt)

        result = await session.execute(stmt)
        instance = result.scalar_one_or_none()
        if not instance:
            raise ValueError(f"{cls.__name__} with id {id} not found")
        return instance

    @classmethod
    async def get_from_id(
        cls: Type[T],
        session: AsyncSession,
        id: int,
        include_deleted: bool = False
    ) -> Optional[T]:
        """
        Get an instance by ID, return None if not found.
        Optional: include soft-deleted rows.
        """
        stmt = select(cls).where(cls.id == id)
        if not include_deleted and hasattr(cls, "deleted_at"):
            stmt = cls._soft_delete_filter(stmt)

        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls: Type[T], session: AsyncSession, include_deleted: bool = False) -> Sequence[T]:
        stmt = select(cls)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one_by(cls: Type[T], session: AsyncSession, include_deleted: bool = False, **kwargs) -> Optional[T]:
        stmt = select(cls).filter_by(**kwargs).limit(1)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def filter_by(cls: Type[T], session: AsyncSession, include_deleted: bool = False, **kwargs) -> Sequence[T]:
        stmt = select(cls).filter_by(**kwargs)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one_via_join(
        cls: Type[T],
        session: AsyncSession,
        join_model: Any,
        where: Optional[ColumnElement[bool]] = None,
        include_deleted: bool = False
    ) -> Optional[T]:
        stmt = cls._set_stmt(
            join_model=join_model,
            where=where,
            include_deleted=include_deleted
        )

        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def filter_via_join(
        cls: Type[T],
        session: AsyncSession,
        join_model: Any,
        where: Optional[ColumnElement[bool]] = None,
        include_deleted: bool = False,
    ) -> Sequence[T]:
        stmt = cls._set_stmt(
            join_model=join_model,
            where=where,
            include_deleted=include_deleted
        )
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    def _set_stmt(cls: Type[T],
                  join_model: Any,
                  where: Optional[ColumnElement[bool]] = None,
                  include_deleted: bool = False) -> Select:
        stmt: Select = select(cls).join(join_model)
        if where is not None:
            stmt = stmt.where(where)

        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)

        return stmt

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

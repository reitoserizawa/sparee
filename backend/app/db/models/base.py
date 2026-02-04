from typing import Optional, Sequence, Type
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.db.database import Base
from sqlalchemy.ext.asyncio import (
    AsyncSession,
)


class BaseModel(Base):
    __abstract__ = True

    async def save(self, session: AsyncSession) -> "BaseModel":
        try:
            session.add(self)
            await session.commit()
            return self
        except SQLAlchemyError:
            await session.rollback()
            raise

    @classmethod
    def _soft_delete_filter(cls, stmt) -> "BaseModel":
        """Automatically add deleted_at is None filter"""
        if hasattr(cls, "deleted_at"):
            stmt = stmt.where(cls.deleted_at.is_(None))
        return stmt

    @classmethod
    async def get_or_raise(
        cls: Type["BaseModel"],
        session: AsyncSession,
        id: int,
        include_deleted: bool = False
    ) -> "BaseModel":
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
        cls: Type["BaseModel"],
        session: AsyncSession,
        id: int,
        include_deleted: bool = False
    ) -> Optional["BaseModel"]:
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
    async def get_all(cls, session: AsyncSession, include_deleted: bool = False) -> Sequence["BaseModel"]:
        stmt = select(cls)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def find_one_by(cls, session: AsyncSession, include_deleted: bool = False, **kwargs) -> Optional["BaseModel"]:
        stmt = select(cls).filter_by(**kwargs).limit(1)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def filter_by(cls, session: AsyncSession, include_deleted: bool = False, **kwargs) -> Sequence["BaseModel"]:
        stmt = select(cls).filter_by(**kwargs)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def soft_delete(self, session: AsyncSession) -> None:
        if hasattr(self, "deleted_at"):
            self.deleted_at = datetime.now(timezone.utc)
            await self.save(session)

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

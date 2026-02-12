from typing import Optional, Sequence, Type, TypeVar, Any, Iterable
from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.orm import selectinload
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

    async def with_relations(
        self: "BaseModel",
        session: AsyncSession,
        relations: Optional[list[str]] = None
    ) -> "BaseModel":
        query = select(self.__class__).where(self.__class__.id == self.id)
        if relations:
            for rel in relations:
                query = query.options(selectinload(
                    getattr(self.__class__, rel)))

        result = await session.execute(query)
        return result.scalar_one()

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
        where: Optional[Iterable[ColumnElement[bool]]] = None,
        order_by: Optional[Iterable[ColumnElement[Any]]] = None,
        include_deleted: bool = False
    ) -> Optional[T]:
        stmt = cls._set_stmt(
            join_model=join_model,
            where=where,
            order_by=order_by,
            include_deleted=include_deleted
        )

        result = await session.execute(stmt)
        return result.scalar_one_or_none()

    @classmethod
    async def filter_via_join(
        cls: Type[T],
        session: AsyncSession,
        join_model: Any,
        where: Optional[Iterable[ColumnElement[bool]]] = None,
        order_by: Optional[Iterable[ColumnElement[Any]]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        include_deleted: bool = False,
    ) -> Sequence[T]:
        stmt = cls._set_stmt(
            join_model=join_model,
            where=where,
            order_by=order_by,
            limit=limit,
            offset=offset,
            include_deleted=include_deleted
        )
        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    def _set_stmt(cls: Type[T],
                  join_model: Any,
                  where: Optional[Iterable[ColumnElement[bool]]] = None,
                  order_by: Optional[Iterable[ColumnElement[Any]]] = None,
                  limit: Optional[int] = None,
                  offset: Optional[int] = None,
                  include_deleted: bool = False) -> Select:
        stmt: Select = select(cls).join(join_model)
        if where is not None:
            stmt = stmt.where(*where)
        if order_by is not None:
            stmt = stmt.order_by(*order_by)
        if limit:
            stmt = stmt.limit(limit)
        if offset:
            stmt = stmt.offset(offset)
        if not include_deleted:
            stmt = cls._soft_delete_filter(stmt)

        return stmt

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

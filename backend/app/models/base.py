from app.database import db
from app.queries import SoftDeleteQuery
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from typing import Type, List, TypeVar, Optional

T = TypeVar("T", bound="BaseModel")


class BaseModel(db.Model):
    __abstract__: bool = True
    query_class: Type[SoftDeleteQuery] = SoftDeleteQuery
    query: SoftDeleteQuery

    def save(self) -> "BaseModel":
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @classmethod
    def get_or_raise(cls: Type[T], id: int) -> T:
        instance = cls.query.get(id)
        if not instance:
            raise ValueError(f"{cls.__name__} with id {id} not found")
        return instance

    @classmethod
    def get_from_id(cls: Type[T], id: int) -> Optional[T]:
        return cls.query.get(id)

    @classmethod
    def get_all(cls: Type[T]) -> List[T]:
        return cls.query.all()

    @classmethod
    def find_one_by(cls: Type[T], **kwargs) -> Optional[T]:
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def find_one_by_or_raise(cls: Type[T], **kwargs) -> T:
        instance = cls.find_one_by(**kwargs)
        if not instance:
            raise ValueError(f"{cls.__name__} not found for {kwargs}")
        return instance

    @classmethod
    def filter_by(cls: Type[T], **kwargs) -> List[T]:
        return cls.query.filter_by(**kwargs).all()

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

    def soft_delete(self) -> None:
        if hasattr(self, 'deleted_at'):
            self.deleted_at = self.set_utc_now()
            self.save()

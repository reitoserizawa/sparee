from app.database import db
from app.queries import SoftDeleteQuery
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone
from typing import Type


class BaseModel(db.Model):
    __abstract__: bool = True
    query_class: Type[SoftDeleteQuery] = SoftDeleteQuery
    query: SoftDeleteQuery

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

    def soft_delete(self) -> None:
        if hasattr(self, 'deleted_at'):
            self.deleted_at = self.set_utc_now()
            self.save()

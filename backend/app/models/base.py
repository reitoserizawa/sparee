from app.database import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone


class BaseModel(db.Model):
    __abstract__ = True

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @classmethod
    def active(cls):
        if hasattr(cls, "deleted_at"):
            return cls.query.filter(cls.deleted_at.is_(None))
        return cls.query

    @staticmethod
    def set_utc_now() -> datetime:
        return datetime.now(timezone.utc)

    def soft_delete(self) -> None:
        if hasattr(self, 'deleted_at'):
            self.deleted_at = self.set_utc_now()
            self.save()

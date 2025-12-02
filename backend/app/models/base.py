from app.database import db
from sqlalchemy.exc import SQLAlchemyError


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

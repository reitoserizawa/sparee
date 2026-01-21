from typing import Type, Optional, TypeVar

from app.database import db
from app.models.base import BaseModel
from app.models.user_skill import UserSkill

T = TypeVar("T", bound="User")


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    user_skills = db.relationship(UserSkill, back_populates="user")
    skills = db.relationship("Skill", secondary="user_skills", viewonly=True)

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
        nullable=True
    )
    deleted_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True
    )

    @classmethod
    def get_by_email(cls: Type[T], email: str) -> Optional[T]:
        return cls.query.filter_by(email=email).first()

    def __repr__(self):
        return f"<User id={self.id} username={self.username} email={self.email}>"

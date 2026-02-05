from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.skill import Skill


class UserSkill(BaseModel):
    __tablename__ = "user_skills"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        "users.id"), primary_key=True)
    user: Mapped["User"] = relationship("User", back_populates="user_skills")

    skill_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        "skills.id"), primary_key=True)
    skill: Mapped["Skill"] = relationship(
        "Skill", back_populates="user_skills")

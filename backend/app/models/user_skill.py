from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class UserSkill(BaseModel):
    __tablename__ = "user_skills"

    user_id = Column(Integer, ForeignKey(
        "users.id"), primary_key=True)
    user = relationship("User", back_populates="user_skills")

    skill_id = Column(Integer, ForeignKey(
        "skills.id"), primary_key=True)
    skill = relationship("Skill", back_populates="user_skills")

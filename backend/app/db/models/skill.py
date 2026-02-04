from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.models.base import BaseModel


class Skill(BaseModel):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    job_post_skills = relationship("JobPostSkill", back_populates="skill")
    job_posts = relationship(
        "JobPost", secondary="job_post_skills", viewonly=True)

    user_skills = relationship("UserSkill", back_populates="skill")
    users = relationship("User", secondary="user_skills", viewonly=True)

    def __repr__(self) -> str:
        return f"<Skill id={self.id} name='{self.name}'>"

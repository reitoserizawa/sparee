from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class JobPostSkill(BaseModel):
    __tablename__ = "job_post_skills"

    required = Column(Boolean, default=False, nullable=False)

    job_post_id = Column(Integer, ForeignKey(
        "job_posts.id"), primary_key=True)
    job_post = relationship("JobPost", back_populates="job_post_skills")

    skill_id = Column(Integer, ForeignKey(
        "skills.id"), primary_key=True)
    skill = relationship("Skill", back_populates="job_post_skills")

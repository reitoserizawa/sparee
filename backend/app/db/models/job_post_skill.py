from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.job_post import JobPost
    from app.db.models.skill import Skill


class JobPostSkill(BaseModel):
    __tablename__ = "job_post_skills"

    required: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)

    job_post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("job_posts.id"), primary_key=True)
    job_post: Mapped["JobPost"] = relationship(
        "JobPost", back_populates="job_post_skills")
    skill_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        "skills.id"), primary_key=True)
    skill: Mapped["Skill"] = relationship(
        "Skill", back_populates="job_post_skills")

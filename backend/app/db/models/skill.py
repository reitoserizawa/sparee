from typing import TYPE_CHECKING
from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.job_post_skill import JobPostSkill
    from app.db.models.user_skill import UserSkill
    from app.db.models.job_post import JobPost
    from app.db.models.user import User


class Skill(BaseModel):
    __tablename__ = 'skills'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    job_post_skills: Mapped[list["JobPostSkill"]] = relationship(
        "JobPostSkill", back_populates="skill")
    job_posts: Mapped[list["JobPost"]] = relationship(
        "JobPost", secondary="job_post_skills", viewonly=True)

    user_skills: Mapped[list["UserSkill"]] = relationship(
        "UserSkill", back_populates="skill")
    users: Mapped[list["User"]] = relationship(
        "User", secondary="user_skills", viewonly=True)

    def __repr__(self) -> str:
        return f"<Skill id={self.id} name='{self.name}'>"

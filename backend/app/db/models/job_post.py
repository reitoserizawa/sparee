from typing import Type, Sequence, TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import Integer, ForeignKey, String, DateTime, Text, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.company import Company
    from app.db.models.address import Address
    from app.db.models.job_post_skill import JobPostSkill
    from app.db.models.job_category import JobCategory
    from app.db.models.skill import Skill
    from app.db.models.user_message import UserMessage


class JobPost(BaseModel):
    __tablename__ = 'job_posts'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    job_category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('job_categories.id'), nullable=False)
    job_category: Mapped["JobCategory"] = relationship(
        "JobCategory", backref="job_posts")

    company_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('companies.id'), nullable=False)
    company: Mapped["Company"] = relationship(
        "Company", backref="job_posts")

    salary: Mapped[float] = mapped_column(Float, nullable=False)
    salary_type: Mapped[str] = mapped_column(String(20), default="hourly")

    address_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey('addresses.id'), nullable=True)
    address: Mapped["Address"] = relationship(
        "Address", backref="job_posts")

    job_post_skills: Mapped[list["JobPostSkill"]] = relationship(
        "JobPostSkill", back_populates="job_post")
    skills: Mapped[list["Skill"]] = relationship(
        "Skill", secondary="job_post_skills", viewonly=True)
    user_messages: Mapped[list["UserMessage"]] = relationship(
        "UserMessage",
        back_populates="job_post",
        cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    @classmethod
    async def get_by_company(cls: Type["JobPost"], session: AsyncSession, company: "Company") -> Sequence["JobPost"]:
        return await cls.filter_by(session=session, company_id=company.id)

    @classmethod
    async def filter_by_nearest(cls: Type["JobPost"], session: AsyncSession, user_point: ColumnElement, limit: int = 20) -> Sequence["JobPost"]:
        return await cls.filter_via_join(session=session, join_model=cls.address, where=[Address.location.isnot(None)], order_by=[Address.location.op("<->")(user_point), cls.created_at.desc()], limit=limit)

    def __repr__(self) -> str:
        return f"<JobPost id={self.id} title={self.title}>"

from typing import Type, List, TypeVar

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.base import BaseModel
from app.models.company import Company

T = TypeVar("T", bound="JobPost")


class JobPost(BaseModel):
    __tablename__ = 'job_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)

    job_category_id = Column(Integer, ForeignKey(
        'job_categories.id'), nullable=False)
    job_category = relationship(
        "JobCategory", backref="job_posts")

    company_id = Column(Integer, ForeignKey(
        'companies.id'), nullable=False)
    company = relationship(
        "Company", backref="job_posts")

    salary = Column(Float, nullable=False)
    salary_type = Column(String(20), default="hourly")

    address_id = Column(Integer, ForeignKey(
        'addresses.id'), nullable=True)
    address = relationship(
        "Address", backref="job_posts")

    job_post_skills = relationship("JobPostSkill", back_populates="job_post")
    skills = relationship("Skill", secondary="job_post_skills", viewonly=True)
    user_messages = relationship(
        "UserMessage",
        back_populates="job_post",
        cascade="all, delete-orphan"
    )

    created_at = Column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
        nullable=True
    )
    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    @classmethod
    async def get_by_company(cls: Type[T], session: AsyncSession, company: Company) -> List[T]:
        return await cls.filter_by(session=session, company_id=company.id)

    def __repr__(self) -> str:
        return f"<JobPost id={self.id} title={self.title}>"

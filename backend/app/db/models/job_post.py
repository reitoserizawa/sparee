from typing import Type, Sequence, TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import Integer, ForeignKey, String, DateTime, Text, Float, literal, select, func
from sqlalchemy.orm import query_expression, relationship, Mapped, mapped_column, selectinload, with_expression
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.elements import ColumnElement
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.company import Company
    from app.db.models.user import User
    from app.db.models.address import Address
    from app.db.models.job_post_skill import JobPostSkill
    from app.db.models.job_category import JobCategory
    from app.db.models.skill import Skill
    from app.db.models.job_application import JobApplication
    from app.db.models.conversation import Conversation

JOB_POST_DETAIL_RELATIONS = ["company",
                             "address", "job_category", "applications"]


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
        Integer, ForeignKey('addresses.id'))
    address: Mapped["Address"] = relationship(
        "Address", backref="job_posts")

    job_post_skills: Mapped[list["JobPostSkill"]] = relationship(
        "JobPostSkill", back_populates="job_post")
    skills: Mapped[list["Skill"]] = relationship(
        "Skill", secondary="job_post_skills", viewonly=True)

    conversations: Mapped[list["Conversation"]] = relationship(
        "Conversation",
        back_populates="job_post",
    )

    applications: Mapped[list["JobApplication"]] = relationship(
        "JobApplication",
        back_populates="job_post",
        cascade="all, delete-orphan"
    )
    application_count: Mapped[int] = query_expression(default_expr=literal(0))

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
    async def get_from_company(cls: Type["JobPost"], session: AsyncSession, company: "Company") -> Optional[Sequence["JobPost"]]:
        from app.db.models.job_application import JobApplication

        count_subquery = (
            select(func.count(JobApplication.id))
            .where(JobApplication.job_post_id == cls.id)
            .correlate_except(JobApplication)
            .scalar_subquery()
        )
        return await cls.filter_by(session=session, company_id=company.id, options=[with_expression(cls.application_count, count_subquery)])

    @classmethod
    async def get_from_user(cls: Type["JobPost"], session: AsyncSession, user: "User") -> Optional[Sequence["JobPost"]]:
        from app.db.models.job_application import JobApplication, ACTIVE_STATUSES

        latest_app = (
            select(
                JobApplication,
                func.row_number().over(
                    partition_by=JobApplication.job_post_id,
                    order_by=JobApplication.updated_at.desc()
                ).label("rn")
            )
            .where(JobApplication.user_id == user.id)
            .cte("latest_app")
        )

        stmt = (
            select(JobPost)
            .options(
                selectinload(JobPost.company),
                selectinload(JobPost.address),
                selectinload(JobPost.job_category),
                selectinload(JobPost.applications)
            )
            .join(
                latest_app,
                (latest_app.c.job_post_id == JobPost.id) & (latest_app.c.rn == 1)
            )
            .where(
                latest_app.c.application_status.in_(ACTIVE_STATUSES),
            )
        )

        result = await session.execute(stmt)
        return result.scalars().all()

    @classmethod
    async def filter_by_nearest(cls: Type["JobPost"], session: AsyncSession, user_point: ColumnElement, limit: int = 20) -> Optional[Sequence["JobPost"]]:
        from app.db.models.address import Address

        return await cls.filter_via_join(session=session, join_model=cls.address, where=[Address.location.isnot(None)], order_by=[Address.location.op("<->")(user_point), cls.created_at.desc()], limit=limit, relations=JOB_POST_DETAIL_RELATIONS)

    async def with_detail_relations(self, session: AsyncSession) -> "JobPost":
        return await self.with_relations(session=session, relations=JOB_POST_DETAIL_RELATIONS)

    def __repr__(self) -> str:
        return f"<JobPost id={self.id} title={self.title}>"

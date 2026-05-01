from typing import Type, TYPE_CHECKING, Sequence, Optional, override
from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy import Integer, ForeignKey, DateTime, Index, Enum as SAEnum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseModel
from app.schemas.job_applications import JobApplicationActivityResponse

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_post import JobPost
    from backend.app.db.models.company import Company

JOB_APPLICATION_DETAIL_RELATIONS = ["job_post"]
PRIVATE_JOB_APPLICATION_DETAIL_RELATIONS = ["job_post", "user"]


class JobApplicationStatus(PyEnum):
    APPLIED = "applied"
    REVIEWING = "reviewing"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"


ACTIVE_STATUSES = [
    JobApplicationStatus.APPLIED,
    JobApplicationStatus.REVIEWING,
]


class JobApplication(BaseModel):
    __tablename__ = "job_applications"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    user: Mapped["User"] = relationship(
        "User", back_populates="job_applications")

    job_post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("job_posts.id"), nullable=False
    )
    job_post: Mapped["JobPost"] = relationship(
        "JobPost", back_populates="applications")

    application_status: Mapped[JobApplicationStatus] = mapped_column(
        SAEnum(JobApplicationStatus, name="application_status"),
        default=JobApplicationStatus.APPLIED,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
    )

    __table_args__ = (
        Index(
            "unique_active_application_per_user_job",
            user_id,
            job_post_id,
            unique=True,
            postgresql_where=application_status.in_(ACTIVE_STATUSES)
        ),
    )

    @classmethod
    async def get_from_user(cls: Type["JobApplication"], session: AsyncSession, user: "User") -> Optional[Sequence["JobApplication"]]:
        return await cls.filter_by(session=session, user_id=user.id, relations=JOB_APPLICATION_DETAIL_RELATIONS)

    @classmethod
    async def get_from_company_and_job_post(cls: Type["JobApplication"], session: AsyncSession, company: "Company", job_post: "JobPost") -> Optional[Sequence["JobApplication"]]:
        return await cls.filter_by(session=session, company_id=company.id, job_post_id=job_post.id, relations=PRIVATE_JOB_APPLICATION_DETAIL_RELATIONS)

    @classmethod
    async def get_from_user_and_job_post(cls: Type["JobApplication"], session: AsyncSession, user: "User", job_post: "JobPost") -> Optional["JobApplication"]:
        return await cls.find_one_by(session=session, user_id=user.id, job_post_id=job_post.id, where=[JobApplication.application_status.in_(ACTIVE_STATUSES)])

    @classmethod
    async def get_active_application(cls: Type["JobApplication"], session: AsyncSession, user: "User", job_post: "JobPost") -> Optional["JobApplication"]:
        return await cls.find_one_by(session=session, user_id=user.id, job_post_id=job_post.id, where=[JobApplication.application_status.in_(ACTIVE_STATUSES)])

    @classmethod
    async def get_activity_by_date(cls: Type["JobApplication"], session: AsyncSession, user: "User", start: datetime, end: datetime,) -> Sequence["JobApplicationActivityResponse"]:
        from sqlalchemy import select, func

        stmt = (
            select(
                func.date(cls.created_at).label("created_date"),
                func.date(cls.updated_at).label("updated_date"),
                cls.application_status,
                func.count().label("count"),
            )
            .where(
                cls.user_id == user.id,
                cls.created_at >= start,
                cls.created_at <= end,
            )
            .group_by(func.date(cls.created_at), func.date(cls.updated_at), cls.application_status)
        )

        result = await session.execute(stmt)
        rows = result.all()
        activity_map = {}

        for created_date, updated_date, status, count in rows:
            created_date_str = created_date.isoformat() if hasattr(
                created_date, "isoformat") else str(created_date)
            updated_date_str = updated_date.isoformat() if hasattr(
                updated_date, "isoformat") else str(updated_date)

            # handle created_date
            if start.date() <= created_date <= end.date():
                if created_date_str not in activity_map:
                    activity_map[created_date_str] = {
                        "date": created_date_str, "total": 0}
                created_status = JobApplicationStatus.APPLIED.value
                activity_map[created_date_str][created_status] = activity_map[created_date_str].get(
                    created_status, 0) + count
                activity_map[created_date_str]["total"] += count

            # handle updated_date
            if start.date() <= updated_date <= end.date():
                if updated_date_str not in activity_map:
                    activity_map[updated_date_str] = {
                        "date": updated_date_str, "total": 0}
                current_status = status.value
                activity_map[updated_date_str][current_status] = activity_map[updated_date_str].get(
                    current_status, 0) + count
                activity_map[updated_date_str]["total"] += count

        return sorted(
            [JobApplicationActivityResponse(**data)
             for data in activity_map.values()],
            key=lambda x: x.date
        )

    @override
    async def soft_delete(self: "JobApplication", session: AsyncSession) -> "JobApplication":
        self.application_status = JobApplicationStatus.WITHDRAWN
        return await self.save(session=session)

    async def with_detail_relations(self, session: AsyncSession) -> "JobApplication":
        return await self.with_relations(session=session, relations=JOB_APPLICATION_DETAIL_RELATIONS)

    def is_owned_by(self: "JobApplication", user: "User"):
        return self.user_id == user.id

    def validate_status_change(self, new_status: JobApplicationStatus):
        if self.application_status == JobApplicationStatus.REJECTED and new_status == JobApplicationStatus.ACCEPTED:
            raise ValueError("Cannot accept a rejected application")

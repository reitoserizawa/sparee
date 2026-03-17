from typing import Type, TYPE_CHECKING, Sequence, Optional, override
from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy import Integer, ForeignKey, DateTime, UniqueConstraint, Enum as SAEnum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_post import JobPost

JOB_APPLICATION_DETAIL_RELATIONS = ["job_post"]


class JobApplicationStatus(PyEnum):
    APPLIED = "applied"
    REVIEWING = "reviewing"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"


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

    status: Mapped[JobApplicationStatus] = mapped_column(
        SAEnum(JobApplicationStatus, name="status"),
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
        UniqueConstraint(
            "user_id",
            "job_post_id",
            name="unique_user_per_job_post"
        ),
    )

    @classmethod
    async def get_from_user(cls: Type["JobApplication"], session: AsyncSession, user: "User") -> Optional[Sequence["JobApplication"]]:
        return await cls.filter_by(session=session, user_id=user.id, relations=JOB_APPLICATION_DETAIL_RELATIONS)

    @classmethod
    async def get_from_user_and_job_post(cls: Type["JobApplication"], session: AsyncSession, user: "User", job_post: "JobPost") -> Optional["JobApplication"]:
        return await cls.find_one_by(session=session, user_id=user.id, job_post_id=job_post.id)

    @override
    async def soft_delete(self: "JobApplication", session: AsyncSession) -> "JobApplication":
        self.status = JobApplicationStatus.WITHDRAWN
        return await self.save(session=session)

    async def with_detail_relations(self, session: AsyncSession) -> "JobApplication":
        return await self.with_relations(session=session, relations=JOB_APPLICATION_DETAIL_RELATIONS)

    def is_owned_by(self: "JobApplication", user: "User"):
        return self.user_id == user.id

    def validate_status_change(self, new_status: JobApplicationStatus):
        if self.status == JobApplicationStatus.REJECTED and new_status == JobApplicationStatus.ACCEPTED:
            raise ValueError("Cannot accept a rejected application")

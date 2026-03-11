from typing import TYPE_CHECKING, Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.job_post_service import JobPostService
from app.schemas.job_applications.create import JobApplicationCreateModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_application import JobApplication
    from app.db.models.job_post import JobPost


class JobApplicationService:
    @staticmethod
    async def get_from_user(session: AsyncSession, user: "User") -> Sequence["JobApplication"] | None:
        from app.db.models.job_application import JobApplication
        job_applications = await JobApplication.get_from_user(session=session, user=user)
        return job_applications

    @staticmethod
    async def get_from_user_and_job_post(session: AsyncSession, user: "User", job_post: "JobPost") -> Optional["JobApplication"]:
        from app.db.models.job_application import JobApplication
        job_application = await JobApplication.get_from_user_and_job_post(session=session, user=user, job_post=job_post)
        return job_application

    @staticmethod
    async def create_job_application(session: AsyncSession, data: JobApplicationCreateModel, user: "User") -> "JobApplication":
        job_post = await JobPostService.get_from_id(session=session, id=data.job_post_id)
        job_application = JobApplication(
            user_id=user.id,
            job_post_id=job_post.id
        )
        await job_application.save(session)
        job_application_with_details = await job_application.with_detail_relations(session=session)
        return job_application_with_details

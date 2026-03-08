from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.job_post_service import JobPostService
from app.schemas.job_applications.create import JobApplicationCreateModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_application import JobApplication


class JobApplicationService:
    @staticmethod
    async def create_job_application(session: AsyncSession, data: JobApplicationCreateModel, user: "User") -> "JobApplication":
        job_post = await JobPostService.get_from_id(session=session, id=data.job_post_id)
        job_application = JobApplication(
            user_id=user.id,
            job_post_id=job_post.id
        )
        await job_application.save(session)
        return job_application

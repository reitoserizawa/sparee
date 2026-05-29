from fastapi import HTTPException
from typing import TYPE_CHECKING, Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_applications import JobApplicationCreateModel, JobApplicationActivityResponseModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_application import JobApplication, JobApplicationStatus
    from app.db.models.job_post import JobPost
    from app.db.models.company import Company


class JobApplicationService:
    @staticmethod
    async def get_or_raise(session: AsyncSession, id: int) -> "JobApplication":
        from app.db.models.job_application import JobApplication
        return await JobApplication.get_or_raise(session=session, id=id)

    @staticmethod
    async def get_from_user(session: AsyncSession, user: "User") -> Sequence["JobApplication"] | None:
        from app.db.models.job_application import JobApplication
        job_applications = await JobApplication.get_from_user(session=session, user=user)
        return job_applications

    @staticmethod
    async def get_from_job_post(session: AsyncSession, job_post: "JobPost") -> Sequence["JobApplication"] | None:
        from app.db.models.job_application import JobApplication
        job_applications = await JobApplication.get_from_job_post(session=session, job_post=job_post)
        return job_applications

    @staticmethod
    async def get_from_user_and_job_post(session: AsyncSession, user: "User", job_post: "JobPost") -> Optional["JobApplication"]:
        from app.db.models.job_application import JobApplication
        job_application = await JobApplication.get_from_user_and_job_post(session=session, user=user, job_post=job_post)
        return job_application

    @staticmethod
    async def get_from_user_and_company(session: AsyncSession, user: "User", company: "Company") -> Optional[Sequence["JobApplication"]]:
        from app.db.models.job_application import JobApplication
        job_applications = await JobApplication.get_from_user_and_company(session=session, user=user, company=company)
        return job_applications

    @staticmethod
    async def get_active_application(session: AsyncSession, user: "User", job_post: "JobPost") -> Optional["JobApplication"]:
        from app.db.models.job_application import JobApplication
        job_application = await JobApplication.get_active_application(session=session, user=user, job_post=job_post)
        return job_application

    @staticmethod
    async def get_activity(session: AsyncSession, user: "User", start: str, end: str) -> Optional[Sequence["JobApplicationActivityResponseModel"]]:
        from app.db.models.job_application import JobApplication
        from datetime import datetime

        start_time = datetime.fromisoformat(start)
        end_time = datetime.fromisoformat(end)

        return await JobApplication.get_activity_by_date(
            session=session,
            user=user,
            start=start_time,
            end=end_time,
        )

    @staticmethod
    async def change_application_status(session: AsyncSession, id: int, new_status: str) -> "JobApplication":
        from app.db.models.job_application import JobApplication
        job_application = await JobApplication.get_or_raise(session=session, id=id)
        validated_status = JobApplicationService._validate_application_status(
            status=new_status)
        job_application.validate_status_change(new_status=validated_status)
        job_application.application_status = validated_status
        await job_application.save(session=session)
        return await job_application.with_detail_relations(session=session, is_private=True)

    @staticmethod
    async def soft_delete(session: AsyncSession, id: int, user: "User") -> "JobApplication":
        from app.db.models.job_application import JobApplication
        job_application = await JobApplication.get_or_raise(session=session, id=id)
        if not job_application.is_owned_by(user=user):
            raise HTTPException(
                status_code=403, detail="User is not authorized to delete the application")

        return await job_application.soft_delete(session=session)

    @staticmethod
    async def create_job_application(session: AsyncSession, data: JobApplicationCreateModel, user: "User") -> "JobApplication":
        from app.services.job_post_service import JobPostService
        from app.db.models.job_application import JobApplication

        job_post = await JobPostService.get_from_id(session=session, id=data.job_post_id)
        if await JobApplicationService.get_active_application(session=session, user=user, job_post=job_post):
            raise HTTPException(
                status_code=403,
                detail=f"User has an active application"
            )
        job_application = JobApplication(
            user_id=user.id,
            job_post_id=job_post.id
        )
        await job_application.save(session)
        job_application_with_details = await job_application.with_detail_relations(session=session)
        return job_application_with_details

    @staticmethod
    def is_owned_by_job_post(job_post: "JobPost", application: "JobApplication") -> bool:
        return job_post.id == application.job_post_id

    @staticmethod
    def _validate_application_status(status: str) -> "JobApplicationStatus":
        from app.db.models.job_application import JobApplicationStatus
        try:
            new_status = JobApplicationStatus(status)
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid status: {status}"
            )
        return new_status

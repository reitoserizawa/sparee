from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.job_application_service import JobApplicationService
from app.schemas.job_applications import JobApplicationResponseModel
from app.api.dependencies.user_required import user_required
from app.db.models import User
from app.db.session import get_session

router = APIRouter()
job_application_service = JobApplicationService()


@router.get("", status_code=200, response_model=list[JobApplicationResponseModel])
async def get_user_job_applications(
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session),
):
    job_applications = await job_application_service.get_from_user(session=session, user=user)
    return job_applications

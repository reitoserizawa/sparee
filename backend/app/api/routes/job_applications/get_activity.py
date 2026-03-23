from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.job_application_service import JobApplicationService
from app.schemas.job_applications import JobApplicationActivityResponse
from app.api.dependencies.user_required import user_required
from app.db.models import User
from app.db.session import get_session

router = APIRouter()
job_application_service = JobApplicationService()


@router.get("", status_code=200, response_model=list[JobApplicationActivityResponse])
async def get_activity(
    start: str,
    end: str,
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session),
):
    return await job_application_service.get_activity(
        session=session,
        user=user,
        start=start,
        end=end,
    )

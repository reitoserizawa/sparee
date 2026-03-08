from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_applications import JobApplicationResponseModel, JobApplicationCreateModel
from app.services.job_application_service import JobApplicationService
from app.db.models.user import User
from app.api.dependencies.user_required import user_required
from app.db.session import get_session

router = APIRouter()
job_application_service = JobApplicationService()


@router.post("/", status_code=201, response_model=JobApplicationResponseModel)
async def create_job_application(payload: JobApplicationCreateModel, session: AsyncSession = Depends(get_session), user: User = Depends(user_required)):
    try:
        job_application = await job_application_service.create_job_application(session, data=payload, user=user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return job_application

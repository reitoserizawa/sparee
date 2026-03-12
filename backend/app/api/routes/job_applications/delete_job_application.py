from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_applications import JobApplicationResponseModel
from app.services.job_application_service import JobApplicationService
from app.db.models.user import User
from app.api.dependencies.user_required import user_required
from app.db.session import get_session

router = APIRouter()
job_application_service = JobApplicationService()


@router.delete("/", status_code=201, response_model=JobApplicationResponseModel)
async def delete_job_application(job_application_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(user_required)):
    try:
        job_application = await job_application_service.soft_delete(session, id=job_application_id, user=user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return job_application

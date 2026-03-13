from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_posts import JobPostResponseModel
from app.services.job_post_service import JobPostService
from app.db.models.user import User
from app.api.dependencies.user_required import user_required
from app.db.session import get_session

router = APIRouter()
job_post_service = JobPostService()


@router.delete("", status_code=201, response_model=JobPostResponseModel)
async def delete_job_application(job_post_id: int, session: AsyncSession = Depends(get_session), user: User = Depends(user_required)):
    try:
        job_post = await job_post_service.delete_job_application_from_user(session=session, user=user, id=job_post_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return job_post

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.services.job_post_service import JobPostService
from app.schemas.job_posts import JobPostResponseModel
from app.api.dependencies.user_required import user_required
from app.db.models import User
from app.db.session import get_session

router = APIRouter()
job_post_service = JobPostService()


@router.get("", status_code=200, response_model=JobPostResponseModel)
async def get_job_post_details(
    job_post_id: int,
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session),
):
    job_posts = await job_post_service.get_from_id(session=session, id=job_post_id)
    return job_posts

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


@router.get("/", status_code=200, response_model=list[JobPostResponseModel])
async def get_nearest_job_posts(
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session),
):
    if not lat or not lng:
        raise ValueError(
            "Latitude and longitude are required to fetch nearest job posts")
    job_posts = await job_post_service.get_nearest(session=session, lat=lat, lng=lng)
    return job_posts

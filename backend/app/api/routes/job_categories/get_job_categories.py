from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.job_category_service import JobCategoryService
from app.schemas.job_categories import JobCategoryResponseModel
from app.api.dependencies.user_required import user_required
from app.db.models import User
from app.db.session import get_session

router = APIRouter()
job_category_service = JobCategoryService()


@router.get("/", status_code=200, response_model=list[JobCategoryResponseModel])
async def get_job_categories(
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session),
):
    job_categories = await job_category_service.get_all(session=session)
    return job_categories

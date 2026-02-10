from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.db.models import Company
from app.schemas.job_posts import JobPostCreateModel, JobPostResponseModel
from app.services.job_post_service import JobPostService
from app.api.dependencies import company_required


router = APIRouter()
job_post_service = JobPostService()


@router.post("/", status_code=201, response_model=JobPostResponseModel)
async def create_job_post(payload: JobPostCreateModel, session: AsyncSession = Depends(get_session), company: Company = Depends(company_required)):
    try:
        job_post = await job_post_service.create_job_post(session, company, payload)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

    return job_post

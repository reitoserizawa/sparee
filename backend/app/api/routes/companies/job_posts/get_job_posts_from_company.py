from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.job_posts import JobPostResponseModel
from app.api.dependencies.company_member_required import company_member_required

from app.db.session import get_session

from app.db.models.company_member import CompanyMember
from app.services.company_service import CompanyService
from app.services.job_post_service import JobPostService

router = APIRouter()
company_service = CompanyService()
job_post_service = JobPostService()


@router.get("/", status_code=200, response_model=list[JobPostResponseModel])
async def get_company_details(
    company_id: int,
    _: CompanyMember = Depends(company_member_required),
    session: AsyncSession = Depends(get_session),
):
    company = await company_service.get_or_raise(session=session, company_id=company_id)
    job_posts = await job_post_service.get_from_company(session=session, company=company)

    return job_posts

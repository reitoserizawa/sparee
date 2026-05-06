from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.api.dependencies.company_member_required import company_member_required

from app.schemas.job_applications.response import CompanySimpleJobApplicationResponseModel
from app.services.company_service import CompanyService
from app.services.job_application_service import JobApplicationService
from app.services.job_post_service import JobPostService
from app.db.models.company_member import CompanyMember


router = APIRouter()
company_service = CompanyService()
job_post_service = JobPostService()
job_application_service = JobApplicationService()


@router.get("/", status_code=200, response_model=list[CompanySimpleJobApplicationResponseModel])
async def get_applications(
    company_id: int,
    job_post_id: int,
    _: CompanyMember = Depends(company_member_required),
    session: AsyncSession = Depends(get_session)
):
    company = await company_service.get_or_raise(session=session, id=company_id)
    job_post = await job_post_service.get_from_id(session=session, id=job_post_id)

    if not job_post_service.is_owned_by_company(job_post=job_post, company=company):
        raise HTTPException(
            status_code=403, detail="Job post does not belong to the company")

    applications = await job_application_service.get_from_job_post(session=session, job_post=job_post)
    return applications

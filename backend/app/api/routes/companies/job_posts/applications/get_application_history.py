from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.api.dependencies.company_member_required import company_member_required
from app.api.dependencies import user_required

from app.schemas.job_applications.response import CompanyJobApplicationResponseModel
from app.services.company_service import CompanyService
from app.services.job_application_service import JobApplicationService
from app.services.job_post_service import JobPostService

from app.db.models.company_member import CompanyMember
from app.db.models.user import User


router = APIRouter()
company_service = CompanyService()
job_post_service = JobPostService()
job_application_service = JobApplicationService()


@router.get("", status_code=200, response_model=list[CompanyJobApplicationResponseModel])
async def get_application_details(
    company_id: int,
    application_id: int,
    _: CompanyMember = Depends(company_member_required),
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session)
):
    company = await company_service.get_or_raise(session=session, id=company_id)
    applications = await job_application_service.get_from_user_and_company(session=session, user=user, company=company)

    if applications:
        applications = [
            app for app in applications if app.id != application_id]

    return applications

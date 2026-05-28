from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_applications import JobApplicationResponseModel, JobApplicationCreateModel, JobApplicationUpdateStatusModel
from app.services.job_application_service import JobApplicationService
from app.db.models.user import User
from app.api.dependencies.user_required import user_required
from app.db.session import get_session
from app.api.dependencies.company_member_required import company_member_required
from app.db.models.company_member import CompanyMember

router = APIRouter()
job_application_service = JobApplicationService()


@router.patch("/", status_code=201, response_model=JobApplicationResponseModel)
async def change_job_application_status(
        application_id: int,
        payload: JobApplicationUpdateStatusModel,
        session: AsyncSession = Depends(get_session),
        _: CompanyMember = Depends(company_member_required)):
    try:
        job_application = await job_application_service.change_application_status(session, id=application_id, new_status=payload.new_status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return job_application

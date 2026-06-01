from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.job_applications import JobApplicationResponseModel, JobApplicationUpdateStatusModel
from app.services.job_application_service import JobApplicationService
from app.services.conversation_service import ConversationService
from app.db.session import get_session
from app.api.dependencies.company_member_required import company_member_required
from app.db.models.company_member import CompanyMember

router = APIRouter()
job_application_service = JobApplicationService()
conversation_service = ConversationService()


@router.patch("/", status_code=201, response_model=JobApplicationResponseModel)
async def change_job_application_status(
        application_id: int,
        payload: JobApplicationUpdateStatusModel,
        session: AsyncSession = Depends(get_session),
        _: CompanyMember = Depends(company_member_required)):
    try:
        job_application = await job_application_service.change_application_status(session, id=application_id, new_status=payload.new_status)
        # create conversation if status is not withdrawn
        if not await conversation_service.get_from_job_post_and_applicant(session=session, job_post_id=job_application.job_post.id, applicant_id=job_application.user.id) and payload.new_status != "withdrawn":
            await conversation_service.create_conversation(session=session, job_post_id=job_application.job_post_id, applicant_id=job_application.user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return job_application

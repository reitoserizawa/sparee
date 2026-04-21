from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.companies import CompanyResponseModel
from app.api.dependencies.company_member_required import company_member_required

from app.db.session import get_session

from app.db.models.company_member import CompanyMember
from app.services.company_service import CompanyService

router = APIRouter()
company_service = CompanyService()


@router.get("", status_code=200, response_model=CompanyResponseModel)
async def get_company_details(
    company_id: int,
    _: CompanyMember = Depends(company_member_required),
    session: AsyncSession = Depends(get_session),
):
    company = await company_service.get_or_raise(session=session, company_id=company_id)
    return company

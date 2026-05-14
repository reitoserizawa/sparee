from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.user_required import user_required

from app.schemas.companies.response import SimpleCompanyResponseModel
from app.services.company_service import CompanyService
from app.db.session import get_session
from app.db.models.user import User

router = APIRouter()
company_service = CompanyService()


@router.get("/", status_code=200, response_model=list[SimpleCompanyResponseModel])
async def get_companies(
    user: User = Depends(user_required),
    session: AsyncSession = Depends(get_session),
):
    companies = await company_service.get_from_user(session=session, user=user)
    return companies

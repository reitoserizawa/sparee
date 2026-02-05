from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.companies import CompanyCreateModel, CompanyResponseModel
from app.services.company_service import CompanyService
from app.db.models.user import User
from app.api.dependencies.user_required import user_required
from app.db.session import get_session

router = APIRouter()
company_service = CompanyService()


@router.post("/", status_code=201, response_model=CompanyResponseModel)
async def create_company(payload: CompanyCreateModel, session: AsyncSession = Depends(get_session), user: User = Depends(user_required)):
    try:
        company = await company_service.create_company(session, data=payload, user=user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return CompanyResponseModel.from_orm(company)

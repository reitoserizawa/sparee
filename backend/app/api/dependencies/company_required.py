from fastapi import Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.db.models import User
from app.services.company_service import CompanyService
from app.api.dependencies.user_required import user_required


async def company_required(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(user_required)
):
    companies = await CompanyService.get_from_user(session=session, user=user)
    if not companies:
        raise HTTPException(
            status_code=401, detail="User does not belong to any company")
    return companies

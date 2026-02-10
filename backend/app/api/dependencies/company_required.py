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
    company = await CompanyService.get_from_user(session=session, user=user)
    if not company:
        raise HTTPException(status_code=401, detail="Company access required")
    return company

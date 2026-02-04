from fastapi import Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.services.company_service import CompanyService


async def company_required(
    request: Request,
    session: AsyncSession = Depends(get_session)
):
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    company = await CompanyService.get_from_user(session=session, user=user)
    if not company:
        raise HTTPException(status_code=401, detail="Company access required")
    return company

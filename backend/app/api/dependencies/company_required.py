from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.company_service import CompanyService


async def company_required(
    user=Depends(lambda: None),
    db: AsyncSession = Depends(get_db)
):
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    company = await CompanyService.get_from_user(session=db, user=user)
    if not company:
        raise HTTPException(status_code=401, detail="Company access required")
    return company

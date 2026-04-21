from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.user_required import user_required
from app.db.session import get_session
from app.db.models.user import User
from app.db.models.company_member import CompanyMember


async def company_member_required(
    company_id: int = Path(...),
    session: AsyncSession = Depends(get_session),
    user: User = Depends(user_required),
):
    member = await CompanyMember.find_one_by(
        session=session,
        user_id=user.id,
        company_id=company_id
    )

    if not member:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated"
        )

    return member

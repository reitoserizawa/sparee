from fastapi import Depends, HTTPException, status
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession


async def user_required(session: AsyncSession = Depends(get_db)):
    # Replace this with your actual user-loading logic
    # For example, decode JWT from header, then fetch user from DB
    user = getattr(session, "user", None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not authenticated"
        )
    return user

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users.login import UserLoginModel
from app.services.user_service import UserService
from app.utils.security import Security
from app.db.session import get_session

router = APIRouter()
user_service = UserService()


@router.post("")
async def login_user(
    payload: UserLoginModel,
    session: AsyncSession = Depends(get_session)
):
    # Authenticate user
    user = await user_service.authenticate(
        session, email=payload.email, password=payload.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Generate JWT token
    token = Security.generate_token(user)

    return {"user": user.username, "token": token}

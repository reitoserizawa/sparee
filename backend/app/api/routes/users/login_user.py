from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import UserLoginModel, UserTokenResponseModel
from app.services.user_service import UserService
from app.utils.security import Security, TokenType
from app.db.session import get_session

router = APIRouter()
user_service = UserService()


@router.post("", status_code=200, response_model=UserTokenResponseModel)
async def login_user(
    response: Response,
    payload: UserLoginModel,
    session: AsyncSession = Depends(get_session)
):

    user = await user_service.authenticate(
        session, data=payload
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    refresh_token = Security.generate_token(user, TokenType.REFRESH)
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * Security.REFRESH_EXPIRE_DAYS,
    )

    access_token = Security.generate_token(
        user=user, token_type=TokenType.ACCESS)

    return {"user": user.username, "token": access_token}

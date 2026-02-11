from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.services.user_service import UserService
from app.schemas.users import UserTokenResponseModel
from app.utils.security import Security, TokenType

router = APIRouter()
user_service = UserService()


@router.post("/refresh", status_code=200, response_model=UserTokenResponseModel)
async def refresh_user(
    request: Request,
    response: Response,
    session: AsyncSession = Depends(get_session),
):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Missing refresh token")

    user = await user_service.get_from_jwt(session=session, token=refresh_token, token_type=TokenType.REFRESH)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_refresh = Security.generate_token(user, TokenType.REFRESH)
    response.set_cookie(
        key="refresh_token",
        value=new_refresh,
        httponly=True,
        secure=True,
        samesite="lax",
        max_age=60 * 60 * 24 * Security.REFRESH_EXPIRE_DAYS,
    )
    new_access_token = Security.generate_token(user, TokenType.ACCESS)

    return {"user": user.username, "token": new_access_token}

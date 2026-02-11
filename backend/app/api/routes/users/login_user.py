from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import UserLoginModel, UserTokenResponseModel
from app.services.user_service import UserService
from app.utils.security import Security, TokenType
from app.db.session import get_session

router = APIRouter()
user_service = UserService()


@router.post("", status_code=200, response_model=UserTokenResponseModel)
async def login_user(
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

    token = Security.generate_token(user=user, token_type=TokenType.ACCESS)

    return {"user": user.username, "token": token}

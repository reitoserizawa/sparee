from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.security import Security, TokenType
from app.schemas.users.create import UserCreateModel
from app.schemas.users.response import UserTokenResponseModel
from app.services.user_service import UserService
from app.db.session import get_session

router = APIRouter()
user_service = UserService()


@router.post("/", status_code=201, response_model=UserTokenResponseModel)
async def create_user(
    payload: UserCreateModel,
    session: AsyncSession = Depends(get_session)
):
    # Check if email already exists
    existing = await user_service.get_from_email(session, email=payload.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email {payload.email} already exists"
        )

    user = await user_service.create_user(session, payload)
    token = Security.generate_token(user=user, token_type=TokenType.ACCESS)

    return {"user": user.username, "token": token}

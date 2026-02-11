from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.security import TokenType
from app.services.user_service import UserService


async def load_user(
    request: Request,
    session: AsyncSession,
):
    authorization = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        return None

    token = authorization.split(" ", 1)[1]
    user = await UserService.get_from_jwt(session=session, token=token, token_type=TokenType.ACCESS)
    return user

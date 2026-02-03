from typing import cast

from flask import current_app
from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from app.models.user import User
from app.utils.security import Security

from app.errors.jwt_configuration_error import JWTConfigurationError


class UserService:

    @staticmethod
    async def get_from_jwt(session: AsyncSession, token: str) -> User | None:
        try:
            payload = Security.decode_jwt(token)
            user_id = int(payload['sub'])
            user = await User.get_from_id(session, id=user_id)
            return user
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None

    @staticmethod
    async def get_from_email(session: AsyncSession, email: str) -> User | None:
        return await User.get_by_email(session, email=email)

    @staticmethod
    async def authenticate(session: AsyncSession, email: str, password: str) -> User | None:
        user = await User.get_by_email(session, email=email)
        if user is not None and Security.verify_password(password, cast(str, user.password)):
            return user
        return None

    @staticmethod
    async def create_user(session: AsyncSession, data) -> User:
        user = User(
            username=data["username"],
            email=data["email"],
            password=Security.hash_password(data["password"])
        )
        await user.save(session)
        return user

    def generate_token(self, user) -> str:
        from datetime import datetime, timedelta, timezone
        secret = current_app.config["SECRET_KEY"]

        if not secret:
            raise JWTConfigurationError(None)

        payload = {"sub": user.id, "exp": datetime.now(timezone.utc) +
                   timedelta(hours=1)}
        return jwt.encode(payload, secret, algorithm="HS256")

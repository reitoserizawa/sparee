from sqlalchemy.ext.asyncio import AsyncSession
import jwt
from app.db.models.user import User
from app.utils.security import Security, TokenType
from app.schemas.users import UserCreateModel, UserLoginModel


class UserService:

    @staticmethod
    async def get_from_jwt(session: AsyncSession, token: str, token_type: TokenType) -> User | None:
        try:
            payload = Security.decode_jwt(token=token, token_type=token_type)
            if not payload:
                return None
            user_id = int(payload['sub'])
            user = await User.get_from_id(session, id=user_id)
            return user
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, ValueError):
            return None

    @staticmethod
    async def get_from_email(session: AsyncSession, email: str) -> User | None:
        return await User.get_by_email(session, email=email)

    @staticmethod
    async def authenticate(session: AsyncSession, data: UserLoginModel) -> User | None:
        user = await User.get_by_email(session, email=data.email)
        if user is not None and Security.verify_password(password=data.password.get_secret_value(), hashed=user.password):
            return user
        return None

    @staticmethod
    async def create_user(session: AsyncSession, data: UserCreateModel) -> User:
        user = User(
            username=data.username,
            email=data.email,
            password=Security.hash_password(data.password.get_secret_value())
        )
        await user.save(session)
        return user

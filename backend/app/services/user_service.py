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
            user_with_companies = await user.with_companies(session) if user else None
            return user_with_companies
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, KeyError, ValueError):
            return None

    @staticmethod
    async def get_from_email(session: AsyncSession, email: str) -> User | None:
        user = await User.get_from_email(session, email=email)
        user_with_companies = await user.with_companies(session) if user else None
        return user_with_companies

    @staticmethod
    async def authenticate(session: AsyncSession, data: UserLoginModel) -> User | None:
        user = await User.get_from_email(session, email=data.email)
        if user is not None and Security.verify_password(password=data.password.get_secret_value(), hashed=user.password):
            return await user.with_companies(session) if user else None
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

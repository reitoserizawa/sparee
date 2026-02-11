import os
from app.errors.jwt_configuration_error import JWTConfigurationError
import bcrypt
import jwt
from typing import Any, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from app.db.models.user import User


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"


class Security:
    ACCESS_EXPIRE_HOURS = 1
    REFRESH_EXPIRE_DAYS = 7

    @staticmethod
    def decode_jwt(token: str, token_type: TokenType) -> Any:
        secret = os.getenv("SECRET_KEY") if token_type == TokenType.ACCESS else os.getenv(
            "REFRESH_SECRET_KEY")

        if not secret:
            raise JWTConfigurationError(None)

        try:
            payload = jwt.decode(
                token,
                secret,
                algorithms=["HS256"],
                options={'require': ['exp', 'sub', 'type']}
            )
            if payload.get("type") != token_type.value:
                return None
            return payload
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return None

    @staticmethod
    def hash_password(password: str) -> str:
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

    @staticmethod
    def generate_token(user: User, token_type: TokenType) -> str:
        from datetime import datetime, timedelta, timezone
        secret = os.getenv("SECRET_KEY") if token_type == TokenType.ACCESS else os.getenv(
            "REFRESH_SECRET_KEY")

        if not secret:
            raise JWTConfigurationError(None)

        payload = {"sub": str(user.id), "type": token_type.value, "exp": datetime.now(timezone.utc) +
                   timedelta(hours=Security.ACCESS_EXPIRE_HOURS if token_type == TokenType.ACCESS else Security.REFRESH_EXPIRE_DAYS * 24)}
        return jwt.encode(payload, secret, algorithm="HS256")

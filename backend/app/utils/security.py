from flask import current_app
from app.errors.jwt_configuration_error import JWTConfigurationError
import bcrypt
import jwt
from typing import Any


class Security:
    @staticmethod
    def decode_jwt(token: str) -> Any:
        secret = current_app.config["SECRET_KEY"]

        try:
            payload = jwt.decode(
                token,
                secret,
                algorithms=["HS256"],
                options={'require': ['exp', 'sub']}
            )
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
    def generate_token(user) -> str:
        from datetime import datetime, timedelta, timezone
        secret = current_app.config["SECRET_KEY"]

        if not secret:
            raise JWTConfigurationError(None)

        payload = {"sub": str(user.id), "exp": datetime.now(timezone.utc) +
                   timedelta(hours=1)}
        return jwt.encode(payload, secret, algorithm="HS256")

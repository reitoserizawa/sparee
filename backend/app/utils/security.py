from flask import current_app
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

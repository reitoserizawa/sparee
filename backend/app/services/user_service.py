from flask import current_app
import jwt
from app.models.user import User
from app.utils.security import Security

from app.errors.jwt_configuration_error import JWTConfigurationError


class UserService:
    def get_from_jwt(self, token: str) -> User | None:
        secret = current_app.config["SECRET_KEY"]

        if not secret:
            raise JWTConfigurationError(None)

        try:
            payload = jwt.decode(
                token,
                secret,
                algorithm="HS256",
                options={'required': ['exp', 'sub']}
            )
            user_id = payload.get('sub')

            return User.get_from_id(id=user_id)
        except (jwt.ExpiredSignatureError or jwt.InvalidTokenError):
            return None

    def authenticate(self, email: str, password: str) -> User | None:
        user = User.get_by_email(email=email)
        if user and Security.verify_password(password, user.password):
            return user
        return None

    def generate_token(self, user) -> str:
        from datetime import datetime, timedelta, timezone
        secret = current_app.config["SECRET_KEY"]

        if not secret:
            raise JWTConfigurationError(None)

        payload = {"sub": user.id, "exp": datetime.now(timezone.utc) +
                   timedelta(hours=1)}
        return jwt.encode(payload, secret, algorithm="HS256")

    def create_user(self, data) -> User:
        user = User()
        user.username = data["username"]
        user.email = data["email"]
        user.password = Security.hash_password(data["password"])
        user.save()
        return user

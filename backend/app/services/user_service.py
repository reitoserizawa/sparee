from flask import current_app
from app.models.user import User
from app.utils.security import Security


class UserService:
    def authenticate(self, email: str, password: str) -> User | None:
        user = User.query.filter_by(email=email).first()
        if user and Security.verify_password(password, user.password):
            return user
        return None

    def generate_token(self, user) -> str:
        import jwt
        from datetime import datetime, timedelta, timezone
        secret = current_app.config["SECRET_KEY"]
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

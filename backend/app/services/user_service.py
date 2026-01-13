from app.models.user import User
from app.utils.security import hash_password


class UserService:
    def create_user(self, data) -> User:
        user = User()
        user.username = data["username"]
        user.email = data["email"]
        user.password = hash_password(data["password"])
        user.save()
        return user

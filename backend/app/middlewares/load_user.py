from flask import g, request
from app.services.user_service import UserService

user_service = UserService()


async def load_user():
    g.user = None

    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        return

    token = auth.split(" ", 1)[1]
    session = g.session
    user = await user_service.get_from_jwt(session, token)
    if user:
        g.user = user

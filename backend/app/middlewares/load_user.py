from flask import g, request
from app.services.user_service import UserService
from typing import Optional
from flask.typing import ResponseReturnValue


def load_user() -> Optional[ResponseReturnValue]:
    g.user = None

    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith('Bearer '):
        return

    token = auth.split(' ', 1)[1]
    g.user = UserService().get_from_jwt(token)

from flask import g, request, current_app
from app.services.user_service import UserService


def load_user(request):
    g.user = None

    auth = request.headers.get('Authorization')
    if not auth or not auth.startswith('Bearer '):
        return

    token = auth.split(' ', 1)[1]
    g.user = UserService().get_from_jwt(token)

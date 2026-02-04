from .create_user import bp as create_user_bp
from .login_user import bp as login_user_bp

USER_BLUEPRINTS = [create_user_bp, login_user_bp]

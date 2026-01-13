from app.routes.users import create_user_bp


def register_blueprints(app):
    app.register_blueprint(create_user_bp)

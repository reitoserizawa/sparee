from app.routes.users import USER_BLUEPRINTS


def register_blueprints(app):
    for bp in USER_BLUEPRINTS:
        app.register_blueprint(bp)

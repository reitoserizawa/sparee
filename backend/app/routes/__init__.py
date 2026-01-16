from app.routes.users import USER_BLUEPRINTS
from app.routes.companies import COMPANY_BLUEPRINTS
from app.routes.addresses import ADDRESS_BLUEPRINTS


def register_blueprints(app):
    for bp in USER_BLUEPRINTS:
        app.register_blueprint(bp)
    for bp in COMPANY_BLUEPRINTS:
        app.register_blueprint(bp)
    for bp in ADDRESS_BLUEPRINTS:
        app.register_blueprint(bp)

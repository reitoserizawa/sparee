from app.routes.register_request_lifecycle import register_request_lifecycle
from app.routes.users import USER_BLUEPRINTS
from app.routes.companies import COMPANY_BLUEPRINTS
from app.routes.addresses import ADDRESS_BLUEPRINTS
from app.routes.job_posts import JOB_POSTS_BLUEPRINTS


def register_blueprints(app):
    register_request_lifecycle(app)

    for bp in USER_BLUEPRINTS:
        app.register_blueprint(bp)
    for bp in COMPANY_BLUEPRINTS:
        app.register_blueprint(bp)
    for bp in ADDRESS_BLUEPRINTS:
        app.register_blueprint(bp)
    for bp in JOB_POSTS_BLUEPRINTS:
        app.register_blueprint(bp)

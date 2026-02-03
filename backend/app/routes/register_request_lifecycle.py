from app.middlewares import load_user, create_session, close_session


def register_request_lifecycle(app):
    app.before_request(create_session)
    app.before_request(load_user)
    app.after_request(close_session)

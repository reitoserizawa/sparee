from functools import wraps
from flask import g, abort


def company_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not g.company:
            abort(401)
        return f(*args, **kwargs)
    return decorated_function

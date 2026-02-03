from functools import wraps
from flask import g, abort


def user_required(f):
    @wraps(f)
    async def wrapper(*args, **kwargs):
        if not g.user:
            abort(401)
        return await f(*args, **kwargs)
    return wrapper

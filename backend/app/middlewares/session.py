from flask import g
from app.database import async_session


async def create_session():
    session = async_session()
    if session is None:
        raise RuntimeError("async_session() returned None")
    g.session = session


async def close_session(response):
    session = g.pop("session", None)
    if session:
        await session.close()
    return response

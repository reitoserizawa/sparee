from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.db.session import AsyncSessionLocal
from app.api.dependencies import load_user


class RequestLifecycleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Create DB session for this request
        async with AsyncSessionLocal() as session:
            request.state.db = session
            request.state.user = await load_user(request=request, session=session)
            response = await call_next(request)
            return response

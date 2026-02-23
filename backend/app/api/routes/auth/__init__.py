from fastapi import APIRouter
from .login import router as login_router
from .refresh import router as refresh_router

router = APIRouter()
router.include_router(login_router, prefix="/login", tags=["auth"])
router.include_router(refresh_router, prefix="/refresh", tags=["auth"])

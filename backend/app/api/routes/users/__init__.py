from fastapi import APIRouter
from .create_user import router as create_user_router
from .profile import router as profile_router

router = APIRouter()
router.include_router(create_user_router, prefix="", tags=["users"])
router.include_router(profile_router, prefix="/profile", tags=["users"])

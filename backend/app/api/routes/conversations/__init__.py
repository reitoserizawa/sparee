from fastapi import APIRouter
from .get_user_conversations import router as get_user_conversations_router

router = APIRouter()
router.include_router(get_user_conversations_router,
                      prefix="", tags=["conversations"])

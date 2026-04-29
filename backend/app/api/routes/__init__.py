from fastapi import APIRouter
from app.api.routes.users import router as users_router
from app.api.routes.companies import router as companies_router
from app.api.routes.addresses import router as addresses_router
from app.api.routes.job_posts import router as job_posts_router
from app.api.routes.auth import router as auth_router
from app.api.routes.job_applications import router as job_application_router
from app.api.routes.chats import router as chat_router
from app.api.routes.job_categories import router as job_categories_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(
    companies_router, prefix="/companies", tags=["companies"])
router.include_router(
    addresses_router, prefix="/addresses", tags=["addresses"])
router.include_router(
    job_posts_router, prefix="/job-posts", tags=["job-posts"])
router.include_router(
    job_application_router, prefix="/job-applications", tags=["job-applications"]
)
router.include_router(
    chat_router, prefix="/chats", tags=["chats"]
)
router.include_router(
    job_categories_router, prefix="/job-categories", tags=["job-categories"]
)

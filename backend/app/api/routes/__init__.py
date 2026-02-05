from fastapi import APIRouter
from app.api.routes.users import router as users_router
from app.api.routes.companies import router as companies_router
from app.api.routes.addresses import router as addresses_router
# from app.api.job_posts import router as job_posts_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(
    companies_router, prefix="/companies", tags=["companies"])
router.include_router(
    addresses_router, prefix="/addresses", tags=["addresses"])
# router.include_router(
#     job_posts_router, prefix="/job_posts", tags=["job_posts"])

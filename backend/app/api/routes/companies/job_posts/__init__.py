from fastapi import APIRouter
from .get_job_posts_from_company import router as get_job_posts_from_company_router

router = APIRouter()

router.include_router(get_job_posts_from_company_router,
                      prefix="", tags=["companies"])

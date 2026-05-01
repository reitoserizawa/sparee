from fastapi import APIRouter
from .get_job_posts_from_company import router as get_job_posts_from_company_router
from .get_job_post_applications import router as get_job_post_applications_router

router = APIRouter()

router.include_router(get_job_posts_from_company_router,
                      prefix="", tags=["job_posts"])
router.include_router(get_job_post_applications_router,
                      prefix="/{job_post_id}/applications", tags=["job_applications"])

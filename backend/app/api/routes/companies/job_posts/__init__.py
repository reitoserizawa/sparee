from fastapi import APIRouter
from .get_job_posts_from_company import router as get_job_posts_from_company_router
from .applications import router as applications_router

router = APIRouter()

router.include_router(get_job_posts_from_company_router,
                      prefix="", tags=["job_posts"])
router.include_router(applications_router,
                      prefix="/{job_post_id}/applications", tags=["job_applications"])

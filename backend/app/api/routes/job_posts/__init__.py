from fastapi import APIRouter
from .create_job_post import router as create_job_post_router
from .get_nearest_job_posts import router as get_nearest_job_posts_router
from .get_job_post import router as get_job_post_router

router = APIRouter()
router.include_router(create_job_post_router, prefix="", tags=["job-posts"])
router.include_router(get_nearest_job_posts_router,
                      prefix="", tags=["job-posts"])
router.include_router(get_job_post_router, prefix="", tags=["job-posts"])

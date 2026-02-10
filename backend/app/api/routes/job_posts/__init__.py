from fastapi import APIRouter
from .create_job_post import router as create_job_post_router

router = APIRouter()
router.include_router(create_job_post_router, prefix="", tags=["job_posts"])

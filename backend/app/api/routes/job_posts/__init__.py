from fastapi import APIRouter
from .create_job_post import router as create_job_post_router
from .get_nearest_job_posts import router as get_nearest_job_posts_router
from .get_job_post_details import router as get_job_post_details_router
from .get_applied_job_posts import router as get_applied_job_posts_router
from .delete_job_application_from_user import router as delete_job_application_from_user_router

router = APIRouter()
router.include_router(create_job_post_router, prefix="", tags=["job-posts"])
router.include_router(get_nearest_job_posts_router,
                      prefix="/nearest", tags=["job-posts"])
router.include_router(get_applied_job_posts_router,
                      prefix="/applied", tags=["job-posts"])
router.include_router(get_job_post_details_router,
                      prefix="/{job_post_id}", tags=["job-posts"])
router.include_router(delete_job_application_from_user_router,
                      prefix="/{job_post_id}", tags=["job-posts"])

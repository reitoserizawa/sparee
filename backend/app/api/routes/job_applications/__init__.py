from fastapi import APIRouter
from .create_job_application import router as create_job_application_router
from .get_user_job_applications import router as get_user_job_applications_router

router = APIRouter()
router.include_router(create_job_application_router,
                      prefix="", tags=["job-applications"])
router.include_router(get_user_job_applications_router,
                      prefix="/me", tags=["job-applications"])

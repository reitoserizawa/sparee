from fastapi import APIRouter
from .create_job_application import router as create_job_application_router

router = APIRouter()
router.include_router(create_job_application_router,
                      prefix="", tags=["job-applications"])

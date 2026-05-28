from fastapi import APIRouter
from .get_applications import router as get_applications_router
from .get_application_details import router as get_application_details_router
from .change_job_application_status import router as change_job_application_status_router

router = APIRouter()

router.include_router(get_applications_router,
                      prefix="", tags=["job_applications"])
router.include_router(get_application_details_router,
                      prefix="/{application_id}", tags=["job_applications"])
router.include_router(change_job_application_status_router,
                      prefix="/{application_id}", tags=["job-applications"])

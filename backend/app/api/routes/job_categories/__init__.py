from fastapi import APIRouter
from .get_job_categories import router as get_job_categories_router


router = APIRouter()
router.include_router(get_job_categories_router,
                      prefix="", tags=["job-categories"])

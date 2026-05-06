from fastapi import APIRouter
from .get_applications import router as get_applications_router

router = APIRouter()

router.include_router(get_applications_router,
                      prefix="", tags=["job_applications"])

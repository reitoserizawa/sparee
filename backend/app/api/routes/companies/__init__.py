from fastapi import APIRouter
from .create_company import router as create_company_router
from .get_company_details import router as get_company_details_router
from .job_posts import router as job_posts_router


router = APIRouter()
router.include_router(create_company_router, prefix="", tags=["companies"])
router.include_router(get_company_details_router,
                      prefix="/{company_id}", tags=["companies"])
router.include_router(job_posts_router,
                      prefix="/{company_id}/job-posts", tags=["companies"])

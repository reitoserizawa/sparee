from fastapi import APIRouter
from .create_company import router as create_company_router

router = APIRouter()
router.include_router(create_company_router, prefix="", tags=["companies"])

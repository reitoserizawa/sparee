from fastapi import APIRouter
from .get_all_addresses import router as get_all_addresses_router

router = APIRouter()
router.include_router(get_all_addresses_router, prefix="", tags=["addresses"])

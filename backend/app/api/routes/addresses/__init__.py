from fastapi import APIRouter
from .get_all_addresses import router as get_all_addresses_bp

router = APIRouter()
router.include_router(get_all_addresses_bp, prefix="", tags=["addresses"])

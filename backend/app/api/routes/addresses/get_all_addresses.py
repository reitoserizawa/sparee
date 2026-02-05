from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.address_service import AddressService
from app.schemas.addresses import AddressResponseModel
from app.db.session import get_session

router = APIRouter()
address_service = AddressService()


@router.get("/", status_code=200, response_model=list[AddressResponseModel])
async def get_all_addresses(session: AsyncSession = Depends(get_session)):
    addresses = await address_service.get_all(session)
    return addresses

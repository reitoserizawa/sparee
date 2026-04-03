from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.address import Address, AddressStatus
from typing import cast, Sequence


class AddressService:
    @staticmethod
    async def get_or_raise(session: AsyncSession, address_id: int) -> Address:
        return await Address.get_or_raise(session, address_id)

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[Address] | None:
        return await Address.get_all(session)

    @staticmethod
    async def create_address(session: AsyncSession, street: str, city: str, state: str, postal_code: str, country: str = "USA") -> Address:
        from app.queues.address_queue import enqueue_geocode
        address = Address(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            geocode_status=AddressStatus.pending
        )
        await address.save(session)
        enqueue_geocode(cast(int, address.id))

        return address

from rq import Retry

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.address import Address
from app.queue import geocode_queue

from app.jobs.address_job import AddressJob

from typing import cast, List


class AddressService:
    @staticmethod
    async def get_or_raise(session: AsyncSession, address_id: int) -> Address:
        return await Address.get_or_raise(session, address_id)

    @staticmethod
    async def get_all(session: AsyncSession) -> List[Address]:
        return await Address.get_all(session)

    @staticmethod
    def enqueue_geocode(address_id: int):
        geocode_queue.enqueue(
            AddressJob.geocode_address_job,
            address_id,
            retry=Retry(max=3, interval=[10, 30, 60]),
            job_timeout=30,
        )

    @staticmethod
    async def create_address(session: AsyncSession, street: str, city: str, state: str, postal_code: str, country: str = "USA") -> Address:
        address = Address(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
        )
        await address.save(session)

        AddressService.enqueue_geocode(cast(int, address.id))

        return address

from rq import Retry

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.address import Address, AddressStatus
from app.workers.job_queue import geocode_queue

from app.workers.jobs.address_job import AddressJob

from typing import cast, Sequence


class AddressService:
    @staticmethod
    async def get_or_raise(session: AsyncSession, address_id: int) -> Address:
        return await Address.get_or_raise(session, address_id)

    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[Address]:
        return await Address.get_all(session)

    @staticmethod
    def enqueue_geocode(address_id: int):
        from app.workers.worker import run_async_job
        geocode_queue.enqueue(
            run_async_job,
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
            geocode_status=AddressStatus.pending
        )
        await address.save(session)

        AddressService.enqueue_geocode(cast(int, address.id))

        return address

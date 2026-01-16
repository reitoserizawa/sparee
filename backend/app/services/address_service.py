from rq import Retry

from app.models.address import Address
from app.queue import geocode_queue

from app.jobs.address_job import AddressJob

from typing import cast, List


class AddressService:
    @staticmethod
    def get_all() -> List[Address]:
        return cast(List[Address], Address.get_all())

    def create_address(self, street: str, city: str, state: str, postal_code: str, country: str = "USA") -> Address:
        address = Address()
        address.street = street
        address.city = city
        address.state = state
        address.postal_code = postal_code
        address.country = country
        address.save()

        geocode_queue.enqueue(
            AddressJob.geocode_address_job,
            address,
            retry=Retry(max=3),
            job_timeout=30,
        )
        return address

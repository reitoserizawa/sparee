from rq import Retry

from app.models.address import Address
from app.queue import geocode_queue

from app.jobs.address_job import AddressJob

from typing import cast, List


class AddressService:
    @staticmethod
    def get_or_raise(address_id: int) -> Address:
        return cast(Address, Address.get_or_raise(address_id))

    @staticmethod
    def get_all() -> List[Address]:
        return cast(List[Address], Address.get_all())

    @staticmethod
    def enqueue_geocode(address_id: int):
        geocode_queue.enqueue(
            AddressJob.geocode_address_job,
            address_id,
            retry=Retry(max=3, interval=[10, 30, 60]),
            job_timeout=30,
        )

    def create_address(self, street: str, city: str, state: str, postal_code: str, country: str = "USA") -> Address:
        address = Address()
        address.street = street
        address.city = city
        address.state = state
        address.postal_code = postal_code
        address.country = country
        address.save()

        self.enqueue_geocode(address.id)

        return address

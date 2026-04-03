from rq import Retry
from app.workers.base_worker import run_async_job
from app.workers.job_queues import geocode_queue
from app.workers.jobs.address_job import AddressJob


def enqueue_geocode(address_id: int):
    geocode_queue.enqueue(
        run_async_job,
        AddressJob.geocode_address_async,
        address_id,
        retry=Retry(max=3, interval=[10, 30, 60]),
        job_timeout=30,
    )

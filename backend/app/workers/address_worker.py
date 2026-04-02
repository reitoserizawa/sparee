from rq import Worker
from app.workers.base_worker import redis_conn, run_async_job
from .job_queues import geocode_queue
from .jobs.address_job import AddressJob


def process_address_job(address_id: int):
    run_async_job(AddressJob.geocode_address_async, address_id)


if __name__ == "__main__":
    worker = Worker([geocode_queue], connection=redis_conn)
    worker.work()

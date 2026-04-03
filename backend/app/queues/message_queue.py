from rq import Retry
from app.workers.base_worker import run_async_job
from app.workers.job_queues import message_queue
from app.workers.jobs.message_job import MessageJob


def enqueue_message(message_data: dict):
    message_queue.enqueue(
        run_async_job,
        MessageJob.save_and_broadcast,
        message_data,
        retry=Retry(max=3, interval=[10, 30, 60]),
        job_timeout=30,
    )

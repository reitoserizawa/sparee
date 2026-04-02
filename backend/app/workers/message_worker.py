from rq import Worker
from .base_worker import redis_conn, run_async_job
from .job_queues import message_queue
from .jobs.message_job import MessageJob


def process_message_job(message_data: dict):
    run_async_job(MessageJob.save_and_broadcast, message_data)


if __name__ == "__main__":
    worker = Worker([message_queue], connection=redis_conn)
    worker.work()

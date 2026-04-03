from rq import Worker
from .base_worker import redis_conn
from .job_queues import message_queue

if __name__ == "__main__":
    worker = Worker([message_queue], connection=redis_conn)
    worker.work()

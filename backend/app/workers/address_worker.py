from rq import Worker
from app.workers.base_worker import redis_conn
from .job_queues import geocode_queue

if __name__ == "__main__":
    worker = Worker([geocode_queue], connection=redis_conn)
    worker.work()

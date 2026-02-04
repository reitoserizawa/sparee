from rq import Worker
from app.workers.job_queue import geocode_queue, redis_conn
import asyncio


def run_async_job(coro, *args, **kwargs):
    """Wrapper to run an async function in the sync RQ worker"""
    asyncio.run(coro(*args, **kwargs))


def main():
    # You might not need FastAPI app itself unless your jobs use it
    worker = Worker([geocode_queue], connection=redis_conn)
    worker.work()


if __name__ == "__main__":
    # RQ is synchronous, so no need for full async loop unless jobs are async
    # If your jobs are async, wrap them properly with asyncio
    main()

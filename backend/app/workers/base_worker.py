import os
import asyncio
from redis import Redis
from rq import Queue

redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis_conn = Redis.from_url(redis_url)


def run_async_job(coro, *args, **kwargs):
    asyncio.run(coro(*args, **kwargs))

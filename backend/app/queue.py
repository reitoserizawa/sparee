from redis import Redis
from rq import Queue
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_conn = Redis.from_url(redis_url)
geocode_queue = Queue("geocode", connection=redis_conn)

from rq import Queue
from .base_worker import redis_conn

geocode_queue = Queue("geocode", connection=redis_conn)
message_queue = Queue("message", connection=redis_conn)

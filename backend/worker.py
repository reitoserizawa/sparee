from rq import Worker
from app import create_app
from app.queue import geocode_queue, redis_conn

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        worker = Worker([geocode_queue], connection=redis_conn)
        worker.work()

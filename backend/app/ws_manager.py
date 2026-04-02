from typing import Dict
from fastapi import WebSocket
from collections import defaultdict


class ConnectionManager:
    def __init__(self):
        # {user_id: set of WebSocket connections}
        self.active_connections: Dict[int, set[WebSocket]] = defaultdict(set)

    async def connect(self, user_id: int, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id].add(websocket)

    def disconnect(self, user_id: int, websocket: WebSocket):
        self.active_connections[user_id].discard(websocket)

    async def send_personal_message(self, user_id: int, message: dict):
        for ws in self.active_connections.get(user_id, []):
            await ws.send_json(message)

    async def broadcast(self, user_ids: list[int], message: dict):
        for user_id in user_ids:
            await self.send_personal_message(user_id, message)

    def start_redis_listener(self):
        from redis import Redis
        from threading import Thread
        import json
        import asyncio

        def run():
            r = Redis.from_url("redis://redis:6379/0")
            pubsub = r.pubsub()
            pubsub.subscribe("messages")

            for msg in pubsub.listen():
                if msg["type"] != "message":
                    continue

                data = json.loads(msg["data"])

                asyncio.run(self.broadcast(
                    data["recipient_ids"],
                    data
                ))

        Thread(target=run, daemon=True).start()


manager = ConnectionManager()
manager.start_redis_listener()

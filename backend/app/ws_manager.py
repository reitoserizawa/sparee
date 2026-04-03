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
            try:
                await ws.send_json(message)
            except Exception:
                self.active_connections[user_id].discard(ws)

    async def broadcast(self, user_ids: list[int], message: dict):
        for user_id in user_ids:
            await self.send_personal_message(user_id, message)

    async def start_redis_listener(self):
        import json
        import asyncio
        from app.workers.base_worker import redis_conn

        pubsub = redis_conn.pubsub()
        pubsub.subscribe("messages")
        while True:
            message = pubsub.get_message(ignore_subscribe_messages=True)
            if message:
                data = json.loads(message["data"])
                recipients = data.get("recipient_ids", []) + \
                    [data.get("sender_id")]
                await self.broadcast(recipients, data)
            await asyncio.sleep(0.01)

    async def shutdown_connections(self):
        for user_id, conns in self.active_connections.items():
            for ws in conns:
                try:
                    await ws.close(code=1001)
                except Exception:
                    pass
        self.active_connections.clear()


manager = ConnectionManager()

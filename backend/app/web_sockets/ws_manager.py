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

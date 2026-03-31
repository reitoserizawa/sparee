from fastapi import APIRouter, WebSocket
from app.web_sockets.ws_manager import ConnectionManager

router = APIRouter()
connection_manager = ConnectionManager()


@router.websocket("")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await connection_manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await connection_manager.send_personal_message(user_id, {"echo": data})
    except Exception:
        connection_manager.disconnect(user_id, websocket)

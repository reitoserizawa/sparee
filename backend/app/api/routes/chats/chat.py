from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.ws_manager import manager

router = APIRouter()


@router.websocket("")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await manager.connect(user_id, websocket)

    try:
        while True:
            data = await websocket.receive_json()
            await manager.send_personal_message(user_id, {
                "type": "echo",
                "data": data
            })

            # TODO: enqueue message job
            # MessageJob.enqueue_message(...)

    except WebSocketDisconnect:
        manager.disconnect(user_id, websocket)
    except Exception:
        manager.disconnect(user_id, websocket)

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from app.ws_manager import manager
from app.api.dependencies.user_required import user_required
from app.db.models import User

router = APIRouter()


@router.websocket("")
async def websocket_endpoint(websocket: WebSocket, conversation_id: int, user: User = Depends(user_required)):
    try:
        await manager.connect(user.id, websocket)

        while True:
            data = await websocket.receive_json()

            # optional test echo back to sender
            await manager.send_personal_message(user, {
                "type": "echo",
                "data": data
            })

            from app.queues.message_queue import enqueue_message

            enqueue_message(
                {
                    "user_id": user.id,
                    "conversation_id": conversation_id,
                    "body": data["body"]
                }
            )

    except WebSocketDisconnect:
        manager.disconnect(user.id, websocket)
    except Exception:
        manager.disconnect(user.id, websocket)

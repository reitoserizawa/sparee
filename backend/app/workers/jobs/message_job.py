import asyncio
import json
from typing import Dict, List

from app.db.session import AsyncSessionLocal
from app.db.models.message import Message
from app.db.models.user_message import UserMessage
from ..base_worker import redis_conn


class MessageJob:
    @staticmethod
    async def save_and_broadcast(message_data: Dict):
        sender_id = message_data["sender_id"]
        recipient_ids: List[int] = message_data.get("recipient_ids", [])
        body = message_data["body"]

        async with AsyncSessionLocal() as session:
            # 1️⃣ Save message
            msg = Message(body=body)
            session.add(msg)
            await session.commit()
            await session.refresh(msg)

            # 2️⃣ Save UserMessage rows
            all_user_ids = [sender_id] + recipient_ids
            for user_id in all_user_ids:
                role = "sender" if user_id == sender_id else "recipient"
                session.add(UserMessage(
                    user_id=user_id,
                    message_id=msg.id,
                    role=role
                ))
            await session.commit()

            # 3️⃣ Publish to Redis (instead of manager.broadcast)
            redis_conn.publish("messages", json.dumps({
                "id": msg.id,
                "body": msg.body,
                "sender_id": sender_id,
                "recipient_ids": recipient_ids
            }))

    @staticmethod
    def enqueue_message(message_data: Dict, queue):
        """
        Enqueue the job into an RQ queue.
        Wraps async save_and_broadcast in asyncio.run for sync RQ worker.
        """
        def job_wrapper(data):
            asyncio.run(MessageJob.save_and_broadcast(data))

        queue.enqueue(job_wrapper, message_data)

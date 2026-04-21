import json

from app.db.session import AsyncSessionLocal
from app.db.models.user import User

from app.schemas.messages.create import MessageCreateModel

from app.services.message_service import MessageService
from app.services.conversation_service import ConversationService
from app.services.conversation_participant import ConversationParticipantService

from ..base_worker import redis_conn


class MessageJob:
    @staticmethod
    async def save_and_broadcast(message_data: dict):
        async with AsyncSessionLocal() as session:
            # create message
            user: User = message_data["user"]
            msg = await MessageService.create_message(
                session=session,
                data=MessageCreateModel(
                    conversation_id=message_data["conversation_id"],
                    body=message_data["body"]
                ),
                user=user
            )

            # add recipients
            conversation = await ConversationService.get_from_id(
                session=session,
                id=message_data["conversation_id"],
                user=user
            )
            pcs = await ConversationParticipantService.get_from_conversation(
                session=session,
                conversation=conversation
            )
            recipient_ids = [
                pc.user_id for pc in pcs if pc.user_id != user.id] if pcs else []

            redis_conn.publish("messages", json.dumps({
                "id": msg.id,
                "body": msg.body,
                "sender_id": msg.sender_id,
                "recipent_ids": recipient_ids,
                "conversation_id": msg.conversation_id,
            }))

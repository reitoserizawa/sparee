from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.messages.create import MessageCreateModel
from app.services.conversation_service import ConversationService

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.message import Message


class MessageService:
    @staticmethod
    async def create_message(session: AsyncSession, data: MessageCreateModel, user: "User") -> "Message":
        conversation = await ConversationService.get_from_id(
            session=session, id=data.conversation_id, user=user)

        if not await conversation.is_participant(session=session, user=user):
            raise ValueError(
                f"User {user.id} is not a participant of conversation {data.conversation_id}")

        message = Message(
            conversation_id=data.conversation_id,
            sender_id=user.id,
            body=data.body
        )
        await message.save(session)
        return message

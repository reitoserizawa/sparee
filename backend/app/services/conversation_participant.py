from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.db.models.conversation import Conversation
from app.db.models.conversation_participant import ConversationParticipant


class ConversationParticipantService:
    @staticmethod
    async def get_from_conversation(session: AsyncSession, conversation: Conversation) -> Optional[Sequence["ConversationParticipant"]]:
        cps = await ConversationParticipant.get_from_conversation(
            session=session,
            conversation=conversation
        )
        return cps

    @staticmethod
    async def add_participant(session: AsyncSession, user: User, conversation: "Conversation") -> "ConversationParticipant":
        cp = ConversationParticipant(
            user_id=user.id, conversation_id=conversation.id)
        return await cp.save(session)

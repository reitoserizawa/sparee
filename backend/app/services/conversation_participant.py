from typing import TYPE_CHECKING, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

if TYPE_CHECKING:
    from app.db.models.conversation import Conversation
    from app.db.models.conversation_participant import ConversationParticipant


class ConversationParticipantService:
    @staticmethod
    async def get_from_conversation(session: AsyncSession, conversation: "Conversation") -> Sequence["ConversationParticipant"]:
        from app.db.models.conversation_participant import ConversationParticipant

        cps = await ConversationParticipant.get_from_conversation(
            session=session,
            conversation=conversation
        )
        return cps

    @staticmethod
    async def bulk_add_participants(
        session: AsyncSession, conversation_id: int, user_ids: list[int]
    ) -> None:
        from app.db.models.conversation_participant import ConversationParticipant

        cps = await ConversationParticipant.bulk_add_participants(session=session, conversation_id=conversation_id, user_ids=user_ids)
        return cps

    @staticmethod
    async def add_participant(session: AsyncSession, user_id: int, conversation: "Conversation") -> "ConversationParticipant":
        from app.db.models.conversation_participant import ConversationParticipant

        cp = ConversationParticipant(
            user_id=user_id, conversation_id=conversation.id)

        return await cp.save(session)

from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.conversations.create import ConversationCreateModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.conversation import Conversation
    from app.db.models.conversation_participant import ConversationParticipant


class ConversationService:
    @staticmethod
    async def get_from_id(session: AsyncSession, id: int, user: "User") -> "Conversation":
        from app.db.models.conversation import Conversation
        conversation = await Conversation.get_or_raise(session=session, id=id)
        if ConversationService._is_participant(session=session, user=user, conversation=conversation):
            return conversation

        raise ValueError(
            f"User {user.id} is not a participant of conversation {id}")

    @staticmethod
    async def get_participants(session: AsyncSession, id: int, user: "User") -> "ConversationParticipant":
        from app.db.models.conversation import Conversation
        from app.db.models.conversation_participant import ConversationParticipant

        conversation = await Conversation.get_or_raise(session=session, id=id)

        if ConversationService._is_participant(session=session, user=user, conversation=conversation):
            return conversation

        raise ValueError(
            f"User {user.id} is not a participant of conversation {id}")

    @staticmethod
    async def create_conversation(session: AsyncSession, data: ConversationCreateModel) -> "Conversation":
        from app.db.models.conversation import Conversation
        conversation = Conversation(
            job_post_id=data.job_post_id,
            applicant_id=data.applicant_id
        )
        await conversation.save(session)
        conversation = await conversation.with_detail_relations(session=session)
        return conversation

    @staticmethod
    async def _is_participant(session: AsyncSession, user: "User", conversation: "Conversation") -> bool:
        from app.db.models.conversation_participant import ConversationParticipant

        return await ConversationParticipant.get_from_user_and_conversation(
            session,
            user=user,
            conversation=conversation
        )

from typing import TYPE_CHECKING, Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from app.services.conversation_participant import ConversationParticipantService

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_post import JobPost
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
    async def get_from_user(session: AsyncSession, user: "User") -> Sequence["Conversation"]:
        from app.db.models.conversation import Conversation

        conversations = await Conversation.get_from_user(session=session, user_id=user.id)
        return conversations

    @staticmethod
    async def get_from_job_post_and_applicant(session: AsyncSession, job_post_id: int, applicant_id: int) -> Optional["Conversation"]:
        from app.db.models.conversation import Conversation
        conversation = await Conversation.get_from_job_post_and_applicant(session=session, job_post_id=job_post_id, applicant_id=applicant_id)
        return conversation

    @staticmethod
    async def get_participant_ids_from_job_post(
        session: AsyncSession, job_post_id: int, applicant_id: int
    ) -> list[int]:
        from app.db.models.company_member import CompanyMember

        cps = await CompanyMember.get_from_job_post(session=session, job_post_id=job_post_id)
        member_ids = [cp.user_id for cp in cps]

        return list(set([applicant_id] + member_ids))

    @staticmethod
    async def create_conversation(session: AsyncSession, job_post_id: int, applicant_id: int) -> "Conversation":
        conversation = Conversation(
            job_post_id=job_post_id,
            applicant_id=applicant_id
        )
        await conversation.save(session)

        participant_ids = await ConversationService.get_participant_ids_from_job_post(
            session, job_post_id, applicant_id
        )
        await ConversationParticipantService.bulk_add_participants(
            session, conversation_id=conversation.id, user_ids=participant_ids
        )

        return await conversation.with_detail_relations(session=session)

    @staticmethod
    async def _is_participant(session: AsyncSession, user: "User", conversation: "Conversation") -> bool:
        from app.db.models.conversation_participant import ConversationParticipant

        return await ConversationParticipant.get_from_user_and_conversation(
            session,
            user_id=user.id,
            conversation_id=conversation.id
        )

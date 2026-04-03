from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_post import JobPost
    from app.db.models.message import Message
    from app.db.models.conversation_participant import ConversationParticipant

CONVERSATION_DETAIL_RELATIONS = ["messages"]


class Conversation(BaseModel):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    job_post_id: Mapped[int] = mapped_column(
        ForeignKey("job_posts.id"), nullable=False, index=True)
    job_post: Mapped["JobPost"] = relationship(
        "JobPost", back_populates="conversations")

    applicant_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, index=True)

    applicant: Mapped["User"] = relationship(
        "User", back_populates="conversations_as_applicant"
    )

    participants: Mapped[list["ConversationParticipant"]] = relationship(
        "ConversationParticipant",
        back_populates="conversation",
    )

    messages: Mapped[list["Message"]] = relationship(
        "Message",
        back_populates="conversation",
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=BaseModel.set_utc_now, nullable=False)

    __table_args__ = (
        UniqueConstraint(
            "applicant_id",
            "job_post_id",
            name="unique_applicant_per_job_post"
        ),
    )

    async def with_detail_relations(self, session: AsyncSession) -> "Conversation":
        return await self.with_relations(session=session, relations=CONVERSATION_DETAIL_RELATIONS)

    async def is_participant(self, session: AsyncSession, user: "User") -> bool:
        from app.db.models.conversation_participant import ConversationParticipant
        conversation = await ConversationParticipant.get_from_user_and_conversation(session=session, user=user, conversation=self)
        return conversation is not None

from typing import TYPE_CHECKING, Sequence, Type, Optional
from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.conversation import Conversation
    from app.db.models.user import User


class ConversationParticipant(BaseModel):
    __tablename__ = "conversation_participants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"), nullable=False, index=True)
    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="participants")

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(
        "User", back_populates="conversation_participants")

    __table_args__ = (
        UniqueConstraint(
            "conversation_id",
            "user_id",
            name="unique_user_per_conversation"
        ),
    )

    @classmethod
    async def get_from_user(cls: Type["ConversationParticipant"], session: AsyncSession, user_id: int) -> Sequence["ConversationParticipant"]:
        cps = await cls.filter_by(
            session=session,
            user_id=user_id
        )
        return cps

    @classmethod
    async def get_from_conversation(
        cls: Type["ConversationParticipant"], session: AsyncSession, conversation: "Conversation"
    ) -> Sequence["ConversationParticipant"]:
        cps = await cls.filter_by(session=session, conversation_id=conversation.id)
        return cps

    @classmethod
    async def get_from_user_and_conversation(cls: Type["ConversationParticipant"], session: AsyncSession, user_id: int, conversation_id: int) -> Optional["ConversationParticipant"]:
        cp = await cls.find_one_by(
            session=session,
            user_id=user_id,
            conversation_id=conversation_id
        )
        return cp

    @staticmethod
    async def bulk_add_participants(
        session: AsyncSession, conversation_id: int, user_ids: list[int]
    ) -> None:
        stmt = insert(ConversationParticipant).values([
            {"conversation_id": conversation_id, "user_id": uid}
            for uid in user_ids
        ]).on_conflict_do_nothing()
        await session.execute(stmt)
        await session.commit()

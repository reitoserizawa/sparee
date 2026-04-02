from typing import TYPE_CHECKING
from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
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

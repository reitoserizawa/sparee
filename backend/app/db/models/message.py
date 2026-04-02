from datetime import datetime
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.models.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.conversation import Conversation


class Message(BaseModel):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    conversation_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("conversations.id", name="fk_messages_conversation_id"), nullable=False, index=True)
    conversation: Mapped["Conversation"] = relationship(
        "Conversation", back_populates="messages")

    sender_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", name="fk_messages_sender_id"), nullable=False, index=True)
    sender: Mapped["User"] = relationship(
        "User", back_populates="sent_messages")

    body: Mapped[str] = mapped_column(String(140), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=BaseModel.set_utc_now, nullable=False,  index=True)

    def __repr__(self) -> str:
        return f'<Message id={self.id} body={self.body}>'

from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.models.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.user_message import UserMessage


class Message(BaseModel):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    body: Mapped[str] = mapped_column(String(140))
    timestamp: Mapped[datetime] = mapped_column(DateTime, index=True,
                                                default=BaseModel.set_utc_now)

    user_messages: Mapped[list["UserMessage"]] = relationship(
        "UserMessage",
        back_populates="message",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'<Message id={self.id} body={self.body}>'

from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.message import Message
    from app.db.models.job_post import JobPost


class UserMessage(BaseModel):
    __tablename__ = "user_messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        "users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="user_messages")
    message_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        "messages.id"), nullable=False)
    message: Mapped["Message"] = relationship(
        "Message", back_populates="user_messages")

    job_post_id: Mapped[int] = mapped_column(Integer, ForeignKey(
        "job_posts.id"), nullable=False)
    job_post: Mapped["JobPost"] = relationship(
        "JobPost", back_populates="user_messages")

    role: Mapped[str] = mapped_column(
        Enum("sender", "recipient", name="message_role"),
        nullable=False
    )

    read_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True))
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True))

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "message_id",
            name="unique_user_per_message"
        ),
    )

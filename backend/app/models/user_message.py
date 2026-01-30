from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class UserMessage(BaseModel):
    __tablename__ = "user_messages"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey(
        "users.id"), nullable=False)
    user = relationship("User", back_populates="user_messages")

    message_id = Column(Integer, ForeignKey(
        "messages.id"), nullable=False)
    message = relationship("Message", back_populates="user_messages")

    job_post_id = Column(Integer, ForeignKey(
        "job_posts.id"), nullable=False)
    job_post = relationship("JobPost", back_populates="user_messages")

    role = Column(
        Enum("sender", "recipient", name="message_role"),
        nullable=False
    )

    read_at = Column(DateTime(timezone=True))
    deleted_at = Column(DateTime(timezone=True))

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "message_id",
            name="unique_user_per_message"
        ),
    )

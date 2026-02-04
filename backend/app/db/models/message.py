from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.models.base import BaseModel


class Message(BaseModel):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    body = Column(String(140))
    timestamp = Column(DateTime, index=True,
                       default=BaseModel.set_utc_now)

    user_messages = relationship(
        "UserMessage",
        back_populates="message",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f'<Message id={self.id} body={self.body}>'

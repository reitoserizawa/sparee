from app.database import db
from app.models.base import BaseModel
from app.models.user_message import UserMessage


class Message(BaseModel):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True,
                          default=BaseModel.set_utc_now)

    deleted_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True
    )

    user_messages = db.relationship(
        "UserMessage",
        back_populates="message",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f'<Message id={self.id} body={self.body}>'

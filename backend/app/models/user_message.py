from app.database import db
from app.models.base import BaseModel


class UserMessage(BaseModel):
    __tablename__ = "user_messages"

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), primary_key=True)
    user = db.relationship("User", back_populates="user_messages")

    message_id = db.Column(db.Integer, db.ForeignKey(
        "messages.id"), primary_key=True)
    message = db.relationship("Message", back_populates="user_messages")

    job_post_id = db.Column(db.Integer, db.ForeignKey(
        "job_posts.id"), primary_key=True)
    job_post = db.relationship("JobPost", back_populates="user_messages")

    role = db.Column(
        db.Enum("sender", "recipient", name="message_role"),
        nullable=False
    )

from app.database import db
from app.models.base import BaseModel


class UserMessage(BaseModel):
    __tablename__ = "user_messages"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    user = db.relationship("User", back_populates="user_messages")

    message_id = db.Column(db.Integer, db.ForeignKey(
        "messages.id"), nullable=False)
    message = db.relationship("Message", back_populates="user_messages")

    job_post_id = db.Column(db.Integer, db.ForeignKey(
        "job_posts.id"), nullable=False)
    job_post = db.relationship("JobPost", back_populates="user_messages")

    role = db.Column(
        db.Enum("sender", "recipient", name="message_role"),
        nullable=False
    )

    read_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True))

    __table_args__ = (
        db.UniqueConstraint(
            "user_id",
            "message_id",
            name="unique_user_per_message"
        ),
    )

from app.database import db
from app.models.base import BaseModel


class UserSkill(BaseModel):
    __tablename__ = "user_skills"

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), primary_key=True)
    user = db.relationship("User", back_populates="user_skills")

    skill_id = db.Column(db.Integer, db.ForeignKey(
        "skills.id"), primary_key=True)
    skill = db.relationship("Skill", back_populates="user_skills")

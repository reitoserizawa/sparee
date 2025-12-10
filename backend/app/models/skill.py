from app.database import db
from app.models.base import BaseModel
from app.models.user import User
from app.models.user_skill import UserSkill


class Skill(BaseModel):
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)

    job_post_skills = db.relationship("JobPostSkill", back_populates="skill")
    job_posts = db.relationship(
        "JobPost", secondary="job_post_skills", viewonly=True)

    user_skills = db.relationship(UserSkill, back_populates="skill")
    users = db.relationship(User, secondary="user_skills", viewonly=True)

    def __repr__(self):
        return f"<Skill id={self.id} name='{self.name}'>"

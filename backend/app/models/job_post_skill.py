from app.database import db
from app.models.base import BaseModel


class JobPostSkill(BaseModel):
    __tablename__ = "job_post_skills"

    required = db.Column(db.Boolean, default=False, nullable=False)

    job_post_id = db.Column(db.Integer, db.ForeignKey(
        "job_posts.id"), primary_key=True)
    job_post = db.relationship("JobPost", back_populates="job_post_skills")

    skill_id = db.Column(db.Integer, db.ForeignKey(
        "skills.id"), primary_key=True)
    skill = db.relationship("Skill", back_populates="job_post_skills")

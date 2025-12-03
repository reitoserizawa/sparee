from app.database import db
from app.models.base import BaseModel
from sqlalchemy.orm import backref


class JobPost(BaseModel):
    __tablename__ = 'job_posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    job_category_id = db.Column(db.Integer, db.ForeignKey(
        'job_categories.id'), nullable=False)
    job_category = db.relationship(
        "JobCategory", backref="job_posts")

    company_id = db.Column(db.Integer, db.ForeignKey(
        'companies.id'), nullable=False)
    company = db.relationship(
        "Company", backref="job_posts")

    created_at = db.Column(
        db.DateTime, default=BaseModel.set_utc_now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=BaseModel.set_utc_now, onupdate=BaseModel.set_utc_now, nullable=True)
    deleted_at = db.Column(
        db.DateTime, nullable=True)

    def __repr__(self):
        return f"<JobPost id={self.id} title={self.title}>"

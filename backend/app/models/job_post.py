from typing import Type, List, TypeVar

from app.database import db
from app.models.job_post_skill import JobPostSkill
from app.models.base import BaseModel
from app.models.address import Address
from app.models.skill import Skill
from app.models.company import Company
from app.models.job_category import JobCategory

T = TypeVar("T", bound="JobPost")


class JobPost(BaseModel):
    __tablename__ = 'job_posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    job_category_id = db.Column(db.Integer, db.ForeignKey(
        'job_categories.id'), nullable=False)
    job_category = db.relationship(
        JobCategory, backref="job_posts")

    company_id = db.Column(db.Integer, db.ForeignKey(
        'companies.id'), nullable=False)
    company = db.relationship(
        Company, backref="job_posts")

    salary = db.Column(db.Float, nullable=False)
    salary_type = db.Column(db.String(20), default="hourly")

    address_id = db.Column(db.Integer, db.ForeignKey(
        'addresses.id'), nullable=True)
    address = db.relationship(
        Address, backref="job_posts")

    job_post_skills = db.relationship(JobPostSkill, back_populates="job_post")
    skills = db.relationship(Skill, secondary="job_post_skills", viewonly=True)

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
        nullable=True
    )
    deleted_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True
    )

    @classmethod
    def get_by_company(cls: Type[T], company: Company) -> List[T]:
        return cls.query.filter_by(company_id=company.id).all()

    def __repr__(self):
        return f"<JobPost id={self.id} title={self.title}>"

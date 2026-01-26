from app.database import db
from app.models.base import BaseModel


class CompanyMember(BaseModel):
    __tablename__ = "company_members"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), primary_key=True)
    user = db.relationship("User", back_populates="company_memberships")

    company_id = db.Column(db.Integer, db.ForeignKey(
        "companies.id"), primary_key=True)
    company = db.relationship("Company", back_populates="members")

from app.database import db
from app.models.base import BaseModel


class CompanyMember(BaseModel):
    __tablename__ = "company_members"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    user = db.relationship("User", back_populates="associated_companies")

    company_id = db.Column(db.Integer, db.ForeignKey(
        "companies.id"), nullable=False)
    company = db.relationship("Company", back_populates="members")

    __table_args__ = (
        db.UniqueConstraint("user_id", "company_id",
                            name="unique_user_company"),
    )

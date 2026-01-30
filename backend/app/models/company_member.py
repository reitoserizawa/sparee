from typing import Optional

from app.database import db
from app.models.base import BaseModel
from app.models.user import User
from app.models.company import Company


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
                            name="unique_user_per_company"),
    )

    @classmethod
    def get_from_user_and_company(cls, user: User, company: Company) -> Optional["CompanyMember"]:
        return cls.find_one_by(
            user_id=user.id,
            company_id=company.id
        )

    @classmethod
    def add_member_or_raise(cls, user: User, company: Company) -> "CompanyMember":
        if cls.get_from_user_and_company(user, company):
            raise ValueError(
                f"User {user.id} is already a member of company {company.id}")

        member = cls()
        member.user_id = user.id
        member.company_id = company.id
        member.save()

        return member

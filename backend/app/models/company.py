from app.database import db
from app.models.base import BaseModel
from app.models.address import Address
from app.models.company_member import CompanyMember
from app.models.user import User


class Company(BaseModel):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'))
    address = db.relationship(Address, backref="companies")

    members = db.relationship(
        CompanyMember,
        back_populates="company",
        cascade="all, delete-orphan"
    )

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

    def __repr__(self) -> str:
        return f"<Company id={self.id} name={self.name}>"

    def add_member(self, user: User) -> CompanyMember:
        return CompanyMember.add_member_or_raise(user, self)

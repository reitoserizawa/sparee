from app.database import db
from app.models.base import BaseModel
from app.models.address import Address
from app.models.company_member import CompanyMember


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

    def __repr__(self):
        return f"<Company id={self.id} name={self.name}>"

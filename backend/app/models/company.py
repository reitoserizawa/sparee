from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.base import BaseModel
from app.models.address import Address
from app.models.company_member import CompanyMember
from app.models.user import User


class Company(BaseModel):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'))
    address = relationship(Address, backref="companies")

    members = relationship(
        CompanyMember,
        back_populates="company",
        cascade="all, delete-orphan"
    )

    created_at = Column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
        nullable=True
    )
    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True
    )

    def __repr__(self) -> str:
        return f"<Company id={self.id} name={self.name}>"

    async def add_member(self, session: AsyncSession, user: User) -> CompanyMember:
        return await CompanyMember.add_member_or_raise(session, user, self)

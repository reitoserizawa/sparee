from typing import TYPE_CHECKING, Optional, Type, Sequence
from sqlalchemy import Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseModel
from datetime import datetime


if TYPE_CHECKING:
    from app.db.models.address import Address
    from app.db.models.company_member import CompanyMember
    from app.db.models.user import User


class Company(BaseModel):
    __tablename__ = 'companies'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('addresses.id'))
    address: Mapped["Address"] = relationship(
        "Address",
        back_populates="companies",
        lazy="selectin"
    )

    members: Mapped[list["CompanyMember"]] = relationship(
        "CompanyMember",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    def __repr__(self) -> str:
        return f"<Company id={self.id} name={self.name}>"

    @classmethod
    async def get_from_user(cls: Type["Company"], session: AsyncSession, user: "User") -> Optional[Sequence["Company"]]:
        from app.db.models.company_member import CompanyMember
        return await cls.filter_via_join(
            session=session,
            join_model=CompanyMember,
            where=[CompanyMember.user_id == user.id]
        )

    async def is_member(self, session: AsyncSession, user: "User") -> bool:
        from app.db.models.company_member import CompanyMember
        member = await CompanyMember.get_from_user_and_company(session=session, user=user, company=self)
        return member is not None

    async def with_address(self, session: AsyncSession) -> "Company":
        return await self.with_relations(session=session, relations=["address"])

    async def add_member(self, session: AsyncSession, user: "User") -> "CompanyMember":
        return await CompanyMember.add_member_or_raise(session=session, user=user, company=self)

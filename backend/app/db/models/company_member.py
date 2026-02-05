from typing import Optional, Type, TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.company import Company


class CompanyMember(BaseModel):
    __tablename__ = "company_members"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship(
        "User", back_populates="associated_companies")

    company_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("companies.id"), nullable=False)
    company: Mapped["Company"] = relationship(
        "Company", back_populates="members")

    __table_args__ = (
        UniqueConstraint("user_id", "company_id",
                         name="unique_user_per_company"),
    )

    @classmethod
    async def get_from_user_and_company(cls: Type["CompanyMember"], session: AsyncSession, user: "User", company: "Company") -> Optional["CompanyMember"]:
        member = await cls.find_one_by(
            session=session,
            user_id=user.id,
            company_id=company.id
        )
        return member

    @classmethod
    async def add_member_or_raise(cls: Type["CompanyMember"], session: AsyncSession, user: "User", company: "Company") -> "CompanyMember":
        existing = await cls.get_from_user_and_company(session=session, user=user, company=company)

        if existing:
            raise ValueError(
                f"User {user.id} is already a member of company {company.id}")

        member = cls(user_id=user.id, company_id=company.id)
        await member.save(session)

        return member

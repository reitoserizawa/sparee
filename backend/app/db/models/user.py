from typing import Type, Optional, TYPE_CHECKING, List
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from app.db.models.base import BaseModel

if TYPE_CHECKING:
    from app.db.models.skill import Skill
    from app.db.models.user_skill import UserSkill
    from app.db.models.company_member import CompanyMember
    from app.db.models.user_message import UserMessage


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(
        String(150), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    user_skills: Mapped[List["UserSkill"]] = relationship(
        "UserSkill", back_populates="user")
    skills: Mapped[List["Skill"]] = relationship(
        "Skill", secondary="user_skills", viewonly=True)

    user_messages: Mapped[List["UserMessage"]] = relationship(
        "UserMessage",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    associated_companies: Mapped[List["CompanyMember"]] = relationship(
        "CompanyMember",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    companies = association_proxy("associated_companies", "company")

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=BaseModel.set_utc_now,
        onupdate=BaseModel.set_utc_now,
        nullable=True
    )
    deleted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )

    @classmethod
    async def get_by_email(cls: Type["User"], session: AsyncSession, email: str) -> Optional["User"]:
        return await cls.find_one_by(session=session, email=email)

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username} email={self.email}>"

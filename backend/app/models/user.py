from typing import Type, Optional, TypeVar
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.base import BaseModel
from app.models.user_skill import UserSkill
from app.models.user_message import UserMessage
from app.models.company_member import CompanyMember

T = TypeVar("T", bound="User")


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    user_skills = relationship(UserSkill, back_populates="user")
    skills = relationship("Skill", secondary="user_skills", viewonly=True)

    user_messages = relationship(
        UserMessage,
        back_populates="user",
        cascade="all, delete-orphan"
    )

    associated_companies = relationship(
        CompanyMember,
        back_populates="user",
        cascade="all, delete-orphan"
    )
    companies = association_proxy("associated_companies", "company")

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

    @classmethod
    async def get_by_email(cls: Type[T], session: AsyncSession, email: str) -> Optional[T]:
        return await cls.find_one_by(session=session, email=email)

    def __repr__(self):
        return f"<User id={self.id} username={self.username} email={self.email}>"

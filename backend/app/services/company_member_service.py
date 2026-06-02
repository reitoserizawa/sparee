from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.company_member import CompanyMember
from app.db.models.company import Company
from app.db.models.user import User


class CompanyMemberService:
    @staticmethod
    async def get_members_from_company(session: AsyncSession, company: Company) -> Sequence[CompanyMember]:
        return await CompanyMember.get_from_company(session, company)

    @staticmethod
    async def add_member(session: AsyncSession, user: User, company: Company) -> CompanyMember:
        return await CompanyMember.add_member_or_raise(session, user, company)

from sqlalchemy.ext.asyncio import AsyncSession
from app.models.company_member import CompanyMember
from app.models.company import Company
from app.models.user import User


class CompanyMemberService:
    @staticmethod
    async def add_member(session: AsyncSession, user: User, company: Company) -> CompanyMember:
        return await CompanyMember.add_member_or_raise(session, user, company)

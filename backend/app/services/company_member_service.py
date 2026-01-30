from app.models.company_member import CompanyMember
from app.models.company import Company
from app.models.user import User


class CompanyMemberService:
    @staticmethod
    def add_member(user: User, company: Company) -> CompanyMember:
        return CompanyMember.add_member_or_raise(user, company)

from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.address_service import AddressService
from app.services.company_member_service import CompanyMemberService
from app.db.models.company import Company
from app.schemas.companies import CompanyCreateModel

if TYPE_CHECKING:
    from app.db.models.company_member import CompanyMember
    from app.db.models.user import User


class CompanyService:
    @staticmethod
    async def get_or_raise(session: AsyncSession, company_id: int) -> "Company":
        return await Company.get_or_raise(session=session, id=company_id)

    @staticmethod
    async def get_from_user(session: AsyncSession, user: "User") -> "Company":
        return await Company.get_from_user(session=session, user=user)

    @staticmethod
    async def create_company(session: AsyncSession, data: CompanyCreateModel, user) -> "Company":
        address_data = data.address
        address = await AddressService.create_address(
            session,
            street=address_data.street,
            city=address_data.city,
            state=address_data.state,
            postal_code=address_data.postal_code,
            country=address_data.country or "USA"
        )
        company_name = data.name
        company = Company(name=company_name, address_id=address.id)
        await company.save(session)
        await CompanyService.add_member(session, company, user)

        return await company.with_address(session)

    @staticmethod
    async def add_member(session: AsyncSession, company: "Company", user: "User") -> "CompanyMember":
        return await CompanyMemberService.add_member(session=session, company=company, user=user)

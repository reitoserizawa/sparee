from typing import TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.address_service import AddressService
from app.services.company_member_service import CompanyMemberService

if TYPE_CHECKING:
    from app.models.company_member import CompanyMember
    from app.models.user import User
    from app.models.company import Company


class CompanyService:
    @staticmethod
    async def get_or_raise(session: AsyncSession, company_id: int) -> "Company":
        return await Company.get_or_raise(session, company_id)

    @staticmethod
    async def create_company(session: AsyncSession, data, user) -> "Company":
        address_data = data.pop("address")
        address = await AddressService.create_address(
            session,
            street=address_data["street"],
            city=address_data["city"],
            state=address_data["state"],
            postal_code=address_data["postal_code"],
            country=address_data.get("country", "USA")
        )

        company = Company(name=data["name"], address_id=address.id)
        await company.save(session)
        await CompanyService.add_member(session, company, user)

        return company

    @staticmethod
    async def add_member(session: AsyncSession, company: "Company", user: "User") -> "CompanyMember":
        return await CompanyMemberService.add_member(session=session, company=company, user=user)

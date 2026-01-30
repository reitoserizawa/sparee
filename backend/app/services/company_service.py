from typing import cast

from app.models.company import Company
from app.models.company_member import CompanyMember
from app.models.user import User
from app.services.address_service import AddressService
from app.services.company_member_service import CompanyMemberService


class CompanyService:
    @staticmethod
    def get_or_raise(company_id: int) -> Company:
        return cast(Company, Company.get_or_raise(company_id))

    def create_company(self, data, user) -> Company:
        # create address first
        address_data = data.pop("address")
        address = AddressService().create_address(
            street=address_data["street"],
            city=address_data["city"],
            state=address_data["state"],
            postal_code=address_data["postal_code"],
            country=address_data.get("country", "USA")
        )

        company = Company()
        company.name = data["name"]
        company.address_id = address.id
        company.save()
        self.add_member(company, user)

        return company

    def add_member(self, company: Company, user: User) -> CompanyMember:
        return CompanyMemberService().add_member(company=company, user=user)

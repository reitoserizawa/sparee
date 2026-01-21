from typing import cast

from app.models.company import Company
from app.services.address_service import AddressService


class CompanyService:
    @staticmethod
    def get_or_raise(company_id: int) -> Company:
        return cast(Company, Company.get_or_raise(company_id))

    def create_company(self, data) -> Company:
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

        return company

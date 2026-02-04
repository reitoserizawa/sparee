from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.job_post import JobPost
from app.db.models.company import Company
from app.services.address_service import AddressService

from typing import Sequence


class JobPostService:
    @staticmethod
    async def get_from_company(session: AsyncSession, company: Company) -> Sequence[JobPost]:
        return await JobPost.get_by_company(session, company)

    @staticmethod
    async def create_job_post(session: AsyncSession, company: Company, data) -> JobPost:
        address_data = data.pop("address", None)
        address = None
        if address_data:
            address = await AddressService.create_address(
                session,
                street=address_data["street"],
                city=address_data["city"],
                state=address_data["state"],
                postal_code=address_data["postal_code"],
                country=address_data.get("country", "USA")
            )
        else:
            address = company.address

        job_post = JobPost(
            session,
            title=data["title"],
            description=data["description"],
            salary=data["salary"],
            salary_type=data.get("salary_type", None),
            job_category_id=data["job_category_id"],
            company_id=company.id,
            address_id=address.id
        )
        await job_post.save(session)

        return job_post

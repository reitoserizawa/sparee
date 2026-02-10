from typing import Sequence, TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from app.services.address_service import AddressService
from app.schemas.job_posts.create import JobPostCreateModel

if TYPE_CHECKING:
    from app.db.models.job_post import JobPost
    from app.db.models.company import Company


class JobPostService:
    @staticmethod
    async def get_from_company(session: AsyncSession, company: Company) -> Sequence[JobPost]:
        return await JobPost.get_by_company(session=session, company=company)

    @staticmethod
    async def create_job_post(session: AsyncSession, company: Company, data: JobPostCreateModel) -> JobPost:
        address_data = data.address
        address = None
        if address_data:
            address = await AddressService.create_address(
                session,
                street=address_data.street,
                city=address_data.city,
                state=address_data.state,
                postal_code=address_data.postal_code,
                country=address_data.country if address_data.country else 'USA'
            )
        else:
            address = company.address

        job_post = JobPost(
            session,
            title=data.title,
            description=data.description,
            salary=data.salary,
            salary_type=data.salary_type,
            job_category_id=data.job_category_id,
            company_id=company.id,
            address_id=address.id if address else None
        )
        await job_post.save(session)

        return job_post

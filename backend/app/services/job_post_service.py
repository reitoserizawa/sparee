from typing import Sequence, TYPE_CHECKING

from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2.functions import ST_SetSRID, ST_MakePoint
from app.services.address_service import AddressService
from app.schemas.job_posts.create import JobPostCreateModel
from app.schemas.addresses.create import AddressCreateModel

if TYPE_CHECKING:
    from app.db.models.user import User
    from app.db.models.job_post import JobPost
    from app.db.models.company import Company
    from app.db.models.address import Address
    from app.db.models.job_category import JobCategory


class JobPostService:
    @staticmethod
    async def get_from_company(session: AsyncSession, company: "Company") -> Sequence["JobPost"]:
        return await JobPost.get_by_company(session=session, company=company)

    @staticmethod
    async def get_nearest(session: AsyncSession, lat: float, lng: float) -> Sequence["JobPost"]:
        from app.db.models.job_post import JobPost
        user_point = ST_SetSRID(ST_MakePoint(lng, lat), 4326)
        job_posts = await JobPost.filter_by_nearest(session=session, user_point=user_point, limit=20)
        return job_posts

    @staticmethod
    async def create_job_post(session: AsyncSession, data: JobPostCreateModel, user: "User") -> "JobPost":
        from app.db.models.job_post import JobPost
        company = await JobPostService._get_company_for_member(session=session, company_id=data.company_id, user=user)
        address = await JobPostService._create_address(session=session, address_data=data.address) if data.address else company.address
        job_category = await JobPostService._get_job_category(session=session, job_category_id=data.job_category_id)

        job_post = JobPost(
            title=data.title,
            description=data.description,
            salary=data.salary,
            salary_type=data.salary_type,
            job_category_id=job_category.id,
            company_id=company.id,
            address_id=address.id
        )
        await job_post.save(session)
        job_post_with_relations = await job_post.with_detail_relations(session=session)

        return job_post_with_relations

    @staticmethod
    async def _get_company_for_member(session: AsyncSession, company_id: int, user: "User") -> "Company":
        from app.db.models.company import Company
        company = await Company.get_from_id(session=session, id=company_id)
        if not company or not await company.is_member(session=session, user=user):
            raise ValueError(
                f"User {user.id} is not a member of company {company_id} or company does not exist")
        return company

    @staticmethod
    async def _get_job_category(session: AsyncSession, job_category_id: int) -> "JobCategory":
        from app.db.models.job_category import JobCategory
        job_category = await JobCategory.get_from_id(session=session, id=job_category_id)
        if not job_category:
            raise ValueError(
                f"Job category with id {job_category_id} does not exist")
        return job_category

    @staticmethod
    async def _create_address(session: AsyncSession, address_data: "AddressCreateModel") -> "Address":
        return await AddressService.create_address(
            session,
            street=address_data.street,
            city=address_data.city,
            state=address_data.state,
            postal_code=address_data.postal_code,
            country=address_data.country if address_data.country else 'USA'
        )

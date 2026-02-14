from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.job_category import JobCategory

JOB_CATEGORIES = [
    "Engineering",
    "Design",
    "Product",
    "Marketing",
    "Sales",
    "Customer Success",
    "Operations",
    "Finance",
    "HR",
]


async def seed_job_categories(session: AsyncSession) -> None:
    for name in JOB_CATEGORIES:
        result = await session.execute(
            select(JobCategory).where(JobCategory.name == name)
        )
        existing = result.scalar_one_or_none()

        if not existing:
            session.add(JobCategory(name=name))

    await session.commit()

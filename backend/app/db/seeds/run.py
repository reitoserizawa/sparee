import asyncio
from app.db.session import AsyncSessionLocal

from .job_category_test import seed_job_categories


async def run():
    async with AsyncSessionLocal() as session:
        await seed_job_categories(session)


if __name__ == "__main__":
    asyncio.run(run())

from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import JobCategory
from typing import cast, Sequence


class JobCategoryService:
    @staticmethod
    async def get_all(session: AsyncSession) -> Sequence[JobCategory] | None:
        return await JobCategory.get_all(session)

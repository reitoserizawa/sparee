from pydantic import Field
from .base import JobCategoryBaseModel


class JobCategoryResponseModel(JobCategoryBaseModel):
    id: int = Field(..., frozen=True)
    name: str = Field(..., frozen=True)

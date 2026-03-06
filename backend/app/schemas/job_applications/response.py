from pydantic import Field
from .base import JobApplicationBaseModel


class JobCategoryResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)
    job_post_id: int = Field(..., frozen=True)
    user_id: int = Field(..., frozen=True)
    status: str = Field(..., frozen=True)

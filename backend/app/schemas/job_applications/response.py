from pydantic import Field
from .base import JobApplicationBaseModel
from ..job_posts import JobPostResponseModel


class JobApplicationResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)
    job_post: JobPostResponseModel = Field(..., frozen=True)
    user_id: int = Field(..., frozen=True)
    status: str = Field(..., frozen=True)

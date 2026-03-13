from typing import TYPE_CHECKING
from pydantic import Field
from .base import JobApplicationBaseModel

if TYPE_CHECKING:
    from ..job_posts import JobPostResponseModel


class JobApplicationResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)
    job_post: "JobPostResponseModel" = Field(..., frozen=True)
    user_id: int = Field(..., frozen=True)
    status: str = Field(..., frozen=True)


class SimpleJobApplicationResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)

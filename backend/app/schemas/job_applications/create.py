from pydantic import Field
from .base import JobApplicationBaseModel


class JobApplicationCreateModel(JobApplicationBaseModel):
    user_id: int = Field(...)
    job_post_id: int = Field(...)

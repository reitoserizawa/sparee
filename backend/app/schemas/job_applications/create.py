from pydantic import Field
from .base import JobApplicationBaseModel


class JobApplicationCreateModel(JobApplicationBaseModel):
    job_post_id: int = Field(...)

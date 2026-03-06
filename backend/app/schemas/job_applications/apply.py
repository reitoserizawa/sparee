from pydantic import Field
from .base import JobApplicationBaseModel


class JobApplicationApplyModel(JobApplicationBaseModel):
    job_post_id: int = Field(...)

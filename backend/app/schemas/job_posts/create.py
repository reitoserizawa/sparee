from pydantic import Field
from .base import JobPostBaseModel
from ..addresses.create import AddressCreateModel


class JobPostCreateModel(JobPostBaseModel):
    title: str = Field(...)
    description: str = Field(...)
    salary: float = Field(...)
    salary_type: str = Field(default='hourly')
    company_id: int = Field(...)
    # has a default salary type value in the model
    job_category_id: int = Field(...)
    address: AddressCreateModel | None = Field(default=None)
    # use company address if not provided

    class Config:
        extra = "forbid"

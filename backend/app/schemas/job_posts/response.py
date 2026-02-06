from pydantic import Field
from .base import JobPostBaseModel
from ..companies.response import CompanyResponseModel
from ..addresses.response import AddressResponseModel


class JobPostResponseModel(JobPostBaseModel):
    id: int = Field(..., frozen=True)

    company: CompanyResponseModel | None = Field(default=None, frozen=True)
    address: AddressResponseModel | None = Field(default=None, frozen=True)
    # job_category: str | None = Field(default=None, frozen=True)
    # skills: list[str] = Field(default_factory=list, frozen=True)

    model_config = {
        "from_attributes": True
    }

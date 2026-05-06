from pydantic import Field
from typing import TYPE_CHECKING
from datetime import datetime
from .base import JobPostBaseModel
from ..companies.response import CompanyResponseModel
from ..addresses.response import AddressResponseModel
from ..job_categories import JobCategoryResponseModel

if TYPE_CHECKING:
    from ..job_applications import SimpleJobApplicationResponseModel


class JobPostResponseModel(JobPostBaseModel):
    id: int = Field(..., frozen=True)

    company: CompanyResponseModel = Field(frozen=True)
    address: AddressResponseModel = Field(frozen=True)
    job_category: JobCategoryResponseModel = Field(frozen=True)
    # skills: list[str] = Field(default_factory=list, frozen=True)

    user_application: "SimpleJobApplicationResponseModel | None" = Field(
        default=None, frozen=True)

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class SimpleJobPostResponseModel(JobPostBaseModel):
    id: int

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class CompanyJobPostResponseModel(SimpleJobPostResponseModel):
    address: AddressResponseModel = Field(frozen=True)
    job_category: JobCategoryResponseModel = Field(frozen=True)


class CompanySimpleJobPostResponseModel(SimpleJobPostResponseModel):
    application_count: int = Field(default=0, frozen=True)

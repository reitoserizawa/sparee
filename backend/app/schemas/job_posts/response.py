from pydantic import Field
from datetime import datetime
from .base import JobPostBaseModel
from ..companies.response import CompanyResponseModel
from ..addresses.response import AddressResponseModel
from ..job_categories import JobCategoryResponseModel
from ..job_applications import SimpleJobApplicationResponseModel


class JobPostResponseModel(JobPostBaseModel):
    id: int = Field(..., frozen=True)

    company: CompanyResponseModel = Field(frozen=True)
    address: AddressResponseModel = Field(frozen=True)
    job_category: JobCategoryResponseModel = Field(frozen=True)
    # skills: list[str] = Field(default_factory=list, frozen=True)

    user_application: SimpleJobApplicationResponseModel | None = Field(
        default=None, frozen=True)

    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

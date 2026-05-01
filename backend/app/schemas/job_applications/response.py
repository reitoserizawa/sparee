from typing import TYPE_CHECKING, Any
from datetime import datetime
from pydantic import Field
from .base import JobApplicationBaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..job_posts import SimpleJobPostResponseModel
    from ..users import SimpleUserResponseModel


class JobApplicationResponseModel(JobApplicationBaseModel):

    id: int = Field(..., frozen=True)
    job_post: "SimpleJobPostResponseModel | None" = Field(
        default=None, frozen=True)
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class SimpleJobApplicationResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class CompanyJobApplicationResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)
    job_post: "SimpleJobPostResponseModel | None" = Field(
        default=None, frozen=True)
    user: "SimpleUserResponseModel | None" = Field(default=None, frozen=True)
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

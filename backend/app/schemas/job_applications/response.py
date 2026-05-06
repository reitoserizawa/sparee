from typing import TYPE_CHECKING, Any
from datetime import datetime
from pydantic import Field

from app.schemas.job_posts.response import CompanyJobPostResponseModel, CompanySimpleJobPostResponseModel
from .base import JobApplicationBaseModel

from typing import TYPE_CHECKING


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
    job_post: CompanyJobPostResponseModel = Field(..., frozen=True)
    user: SimpleUserResponseModel | None = Field(default=None, frozen=True)
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class CompanySimpleJobApplicationResponseModel(JobApplicationBaseModel):
    id: int = Field(..., frozen=True)
    job_post: CompanySimpleJobPostResponseModel | None = Field(
        default=None, frozen=True)
    user: SimpleUserResponseModel | None = Field(default=None, frozen=True)
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

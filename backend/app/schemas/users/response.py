from pydantic import Field, BaseModel
from datetime import datetime
from .base import UserBaseModel
from ..companies.response import CompanyResponseModel


class UserResponseModel(UserBaseModel):
    id: int = Field(..., frozen=True)
    companies: list[CompanyResponseModel] | None = Field(
        default_factory=list, frozen=True)
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }


class UserTokenResponseModel(BaseModel):
    user: UserResponseModel
    access_token: str = Field(..., frozen=True)

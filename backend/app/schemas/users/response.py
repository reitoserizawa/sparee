from datetime import datetime
from pydantic import Field, BaseModel
from .base import UserBaseModel


class UserTokenResponseModel(BaseModel):
    user: str = Field(..., frozen=True)
    token: str = Field(..., frozen=True)


class UserResponseModel(UserBaseModel):
    id: int = Field(..., frozen=True)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

    model_config = {
        "from_attributes": True
    }

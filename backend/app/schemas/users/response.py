from datetime import datetime
from pydantic import Field
from .base import UserBaseModel


class UserResponseModel(UserBaseModel):
    id: int = Field(..., frozen=True)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

    @classmethod
    def from_orm_obj(cls, obj):
        return cls(
            id=obj.id,
            username=obj.username,
            email=obj.email,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
        )

from typing import List
from datetime import datetime
from pydantic import Field
from .base import UserBaseModel


class UserResponseModel(UserBaseModel):
    id: int
    created_at: datetime = Field(..., read_only=True)
    updated_at: datetime = Field(..., read_only=True)
    skills: List[str] = []

    class Config:
        from_attributes = True

    @classmethod
    def from_orm_obj(cls, obj):
        skills = [skill.name for skill in getattr(obj, "skills", []) or []]
        return cls(
            id=obj.id,
            username=obj.username,
            email=obj.email,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
            skills=skills
        )

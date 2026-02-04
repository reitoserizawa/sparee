from pydantic import EmailStr, Field
from .base import UserBaseModel


class UserCreateModel(UserBaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., write_only=True)

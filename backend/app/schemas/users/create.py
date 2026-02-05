from pydantic import EmailStr, Field, SecretStr
from .base import UserBaseModel


class UserCreateModel(UserBaseModel):
    username: str = Field(...)
    email: EmailStr = Field(...)
    password: SecretStr = Field(...)

    class Config:
        extra = "forbid"

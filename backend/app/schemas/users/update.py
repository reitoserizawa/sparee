from pydantic import EmailStr, Field
from .base import UserBaseModel


class UserUpdateModel(UserBaseModel):
    username: str
    email: EmailStr
    password: str = Field(write_only=True)

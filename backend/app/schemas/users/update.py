from pydantic import SecretStr
from .base import UserBaseModel


class UserUpdateModel(UserBaseModel):
    password: SecretStr

    class Config:
        extra = "forbid"

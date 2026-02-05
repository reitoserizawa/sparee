from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserLoginModel(BaseModel):
    email: EmailStr = Field(...)
    password: SecretStr = Field(...)

    class Config:
        extra = "forbid"

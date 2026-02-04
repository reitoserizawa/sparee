from pydantic import BaseModel, EmailStr, Field


class UserLoginModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(..., write_only=True)

    class Config:
        extra = "forbid"

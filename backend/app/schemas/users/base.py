from pydantic import BaseModel, EmailStr


class UserBaseModel(BaseModel):
    username: str
    email: EmailStr

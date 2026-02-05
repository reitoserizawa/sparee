from pydantic import BaseModel


class CompanyBaseModel(BaseModel):
    name: str

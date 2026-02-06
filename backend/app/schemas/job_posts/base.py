from pydantic import BaseModel


class JobPostBaseModel(BaseModel):
    title: str
    description: str
    salary: float
    salary_type: str

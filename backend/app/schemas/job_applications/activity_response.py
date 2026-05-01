from pydantic import BaseModel
from datetime import date


class JobApplicationActivityResponseModel(BaseModel):
    date: date
    total: int

    class Config:
        extra = "allow"

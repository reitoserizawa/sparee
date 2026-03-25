from typing import Optional
from pydantic import BaseModel
from datetime import date


class JobApplicationActivityResponse(BaseModel):
    date: date
    total: int

    class Config:
        extra = "allow"

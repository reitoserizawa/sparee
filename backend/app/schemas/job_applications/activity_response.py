from pydantic import BaseModel
from datetime import date


class JobApplicationActivityResponse(BaseModel):
    date: date
    applied: int
    interviewing: int
    accepted: int
    rejected: int
    total: int

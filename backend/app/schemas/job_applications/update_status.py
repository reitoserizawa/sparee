from pydantic import Field, BaseModel


class JobApplicationUpdateStatusModel(BaseModel):
    new_status: str = Field(...)

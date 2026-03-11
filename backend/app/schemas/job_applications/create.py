from pydantic import Field, BaseModel


class JobApplicationCreateModel(BaseModel):
    job_post_id: int = Field(...)

from pydantic import BaseModel


class JobApplicationBaseModel(BaseModel):
    job_post_id: int

from pydantic import BaseModel


class JobApplicationBaseModel(BaseModel):
    user_id: int
    job_post_id: int
    application_status: str

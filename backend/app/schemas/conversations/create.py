from pydantic import BaseModel, Field


class ConversationCreateModel(BaseModel):
    job_post_id: int = Field(...)
    applicant_id: int = Field(...)

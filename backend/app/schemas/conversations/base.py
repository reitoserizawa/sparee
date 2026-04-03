from pydantic import BaseModel


class ConversationBaseModel(BaseModel):
    job_post_id: int
    applicant_id: int

from datetime import datetime
from pydantic import Field

from app.schemas.job_posts.response import SimpleJobPostResponseModel
from app.schemas.users.response import SimpleUserResponseModel
from .base import ConversationBaseModel
from ..messages.response import MessageResponseModel


class ConversationResponseModel(ConversationBaseModel):
    id: int = Field(..., frozen=True)
    messages: list[MessageResponseModel] = Field(frozen=True)
    applicant: SimpleUserResponseModel
    users: list[SimpleUserResponseModel] = Field(frozen=True)
    job_post: SimpleJobPostResponseModel

    created_at: datetime

    model_config = {
        "from_attributes": True
    }

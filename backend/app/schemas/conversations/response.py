from datetime import datetime
from pydantic import Field
from .base import ConversationBaseModel
from ..messages.response import MessageResponseModel


class ConversationResponseModel(ConversationBaseModel):
    id: int = Field(..., frozen=True)
    messages: list[MessageResponseModel] = Field(frozen=True)
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

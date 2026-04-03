from pydantic import Field
from datetime import datetime
from .base import MessageBaseModel


class MessageResponseModel(MessageBaseModel):
    id: int = Field(..., frozen=True)
    timestamp: datetime

    model_config = {
        "from_attributes": True
    }

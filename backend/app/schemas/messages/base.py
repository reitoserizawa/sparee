from pydantic import BaseModel, Field


class MessageBaseModel(BaseModel):
    conversation_id: int
    sender_id: int
    body: str

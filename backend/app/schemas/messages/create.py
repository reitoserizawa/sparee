from pydantic import BaseModel, Field


class MessageCreateModel(BaseModel):
    conversation_id: int = Field(...)
    body: str = Field(...)

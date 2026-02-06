from pydantic import Field
from .base import SkillBaseModel


class SkillResponseModel(SkillBaseModel):
    id: int = Field(..., frozen=True)

    model_config = {
        "from_attributes": True
    }

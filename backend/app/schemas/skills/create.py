from pydantic import Field
from .base import SkillBaseModel


class SkillCreateModel(SkillBaseModel):
    name: str = Field(...)

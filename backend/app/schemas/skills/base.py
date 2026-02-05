from pydantic import BaseModel


class SkillBaseModel(BaseModel):
    name: str

from marshmallow import fields
from .base import SkillBaseSchema


class SkillCreateSchema(SkillBaseSchema):
    name = fields.Str(required=True)

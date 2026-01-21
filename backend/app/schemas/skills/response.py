from marshmallow import fields
from .base import SkillBaseSchema


class SkillResponseSchema(SkillBaseSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)

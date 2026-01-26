from marshmallow import fields
from .base import UserBaseSchema


class UserResponseSchema(UserBaseSchema):
    id = fields.Int(dump_only=True)

    username = fields.Str(dump_only=True)
    email = fields.Email(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    skills = fields.Method("get_skill_names")

    def get_skill_names(self, obj):
        return [skill.name for skill in obj.skills]

from marshmallow import fields
from .base import UserBaseSchema


class UserResponseSchema(UserBaseSchema):
    id = fields.Int()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    skills = fields.Method("get_skill_names")

    def get_skill_names(self, obj):
        return [skill.name for skill in obj.skills]

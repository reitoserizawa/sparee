from marshmallow import Schema, fields
from ..skills.response import SkillResponseSchema


class UserResponseSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()

    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    skills = fields.Method("get_skill_names")

    def get_skill_names(self, obj):
        return [skill.name for skill in obj.skills]

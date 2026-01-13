from marshmallow import Schema, fields


class SkillResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()

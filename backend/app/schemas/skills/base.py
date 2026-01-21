from marshmallow import Schema, fields


class SkillBaseSchema(Schema):
    name = fields.Str()

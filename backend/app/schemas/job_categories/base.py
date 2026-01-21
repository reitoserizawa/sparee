from marshmallow import Schema, fields


class JobCategoryBaseSchema(Schema):
    name = fields.Str()

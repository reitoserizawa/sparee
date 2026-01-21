from marshmallow import Schema, fields


class JobPostBaseSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    salary = fields.Float()
    salary_type = fields.Str()

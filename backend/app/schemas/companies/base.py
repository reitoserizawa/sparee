from marshmallow import Schema, fields


class CompanyBaseSchema(Schema):
    name = fields.Str()

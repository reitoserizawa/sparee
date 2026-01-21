from marshmallow import fields
from .base import JobCategoryBaseSchema


class JobCategoryResponseSchema(JobCategoryBaseSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(dump_only=True)

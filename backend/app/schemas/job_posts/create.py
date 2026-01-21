from marshmallow import fields
from .base import JobPostBaseSchema
from ..addresses.create import AddressCreateSchema


class JobPostCreateSchema(JobPostBaseSchema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    salary = fields.Float(required=True)
    salary_type = fields.Str(required=False)
    # has a default salary type value in the model
    job_category_id = fields.Int(required=True)
    address = fields.Nested(AddressCreateSchema, required=False)
    # use company address if not provided

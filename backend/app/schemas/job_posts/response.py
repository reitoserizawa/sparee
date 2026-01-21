from marshmallow import fields
from .base import JobPostBaseSchema
from ..companies.response import CompanyResponseSchema
from ..addresses.response import AddressResponseSchema


class JobPostResponseSchema(JobPostBaseSchema):
    id = fields.Int(dump_only=True)
    title = fields.Str(dump_only=True)
    description = fields.Str(dump_only=True)
    salary = fields.Float(dump_only=True)
    salary_type = fields.Str(dump_only=True)
    company = fields.Nested(CompanyResponseSchema, dump_only=True)
    address = fields.Nested(AddressResponseSchema, dump_only=True)
    job_category = fields.Method('get_job_category_name', dump_only=True)
    skills = fields.Method("get_skill_names", dump_only=True)

    def get_job_category_name(self, obj):
        return obj.job_category.name if obj.job_category else None

    def get_skill_names(self, obj):
        return [skill.name for skill in obj.skills]

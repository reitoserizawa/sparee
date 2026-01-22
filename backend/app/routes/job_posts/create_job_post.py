from flask import Blueprint, request, jsonify, g
from marshmallow import ValidationError

from app.schemas.job_posts.create import JobPostCreateSchema
from app.schemas.job_posts.response import JobPostResponseSchema
from app.services.job_post_service import JobPostService

from app.decorators.company_required import company_required
from app.utils.load_dict import load_dict

bp = Blueprint("job_posts", __name__, url_prefix="/api/job_posts")

create_schema = JobPostCreateSchema()
response_schema = JobPostResponseSchema()
job_post_service = JobPostService()


@bp.route("", methods=["POST"])
@company_required
def create_job_post():
    try:
        payload = load_dict(create_schema, request.json)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    company = g.company
    job_post = job_post_service.create_job_post(company, payload)

    return jsonify(response_schema.dump(job_post)), 201

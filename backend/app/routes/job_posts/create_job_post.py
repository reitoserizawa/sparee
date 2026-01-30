from flask import Blueprint, request, jsonify, g
from marshmallow import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.job_posts.create import JobPostCreateSchema
from app.schemas.job_posts.response import JobPostResponseSchema
from app.services.job_post_service import JobPostService

from app.decorators.company_required import company_required
from app.decorators.with_session import with_session
from app.utils.load_dict import load_dict

bp = Blueprint("job_posts", __name__, url_prefix="/api/job_posts")

create_schema = JobPostCreateSchema()
response_schema = JobPostResponseSchema()
job_post_service = JobPostService()


@bp.route("", methods=["POST"])
@with_session
@company_required
async def create_job_post(session: AsyncSession):
    try:
        payload = load_dict(create_schema, request.json)
    except ValidationError as err:
        return {"errors": err.messages}, 400
    company = g.company
    job_post = await job_post_service.create_job_post(session, company, payload)

    return jsonify(response_schema.dump(job_post)), 201

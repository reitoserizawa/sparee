from flask import Blueprint, request, jsonify, g
from sqlalchemy.ext.asyncio import AsyncSession
from marshmallow import ValidationError
from app.schemas.companies.create import CompanyCreateSchema
from app.schemas.companies.response import CompanyResponseSchema
from app.services.company_service import CompanyService
from app.utils.load_dict import load_dict
from app.decorators.user_required import user_required
from app.decorators.with_session import with_session

bp = Blueprint("companies", __name__, url_prefix="/api/companies")

create_schema = CompanyCreateSchema()
response_schema = CompanyResponseSchema()
company_service = CompanyService()


@bp.route("", methods=["POST"])
@with_session
@user_required
async def create_company(session: AsyncSession):
    try:
        payload = load_dict(create_schema, request.json)
    except ValidationError as err:
        return {"errors": err.messages}, 400

    user = g.user
    company = await company_service.create_company(session, data=payload, user=user)

    return jsonify(response_schema.dump(company)), 201

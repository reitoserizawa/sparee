from flask import Blueprint, jsonify
from sqlalchemy.ext.asyncio import AsyncSession
from app.decorators.with_session import with_session
from app.services.address_service import AddressService
from app.schemas.addresses.response import AddressResponseSchema

bp = Blueprint("addresses", __name__, url_prefix="/api/addresses")

response_schema = AddressResponseSchema(many=True)
address_service = AddressService()


@bp.route("/", methods=["GET"])
@with_session
async def get_all_addresses(session: AsyncSession):
    addresses = await address_service.get_all(session)
    return jsonify(response_schema.dump(addresses)), 200

from flask import Blueprint, jsonify, g
from app.services.address_service import AddressService
from app.schemas.addresses.response import AddressResponseSchema

bp = Blueprint("addresses", __name__, url_prefix="/api/addresses")

response_schema = AddressResponseSchema(many=True)
address_service = AddressService()


@bp.route("/", methods=["GET"])
async def get_all_addresses():
    session = g.session
    addresses = await address_service.get_all(session)
    return jsonify(response_schema.dump(addresses)), 200

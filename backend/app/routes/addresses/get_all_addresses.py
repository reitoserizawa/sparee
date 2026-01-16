from flask import Blueprint, jsonify
from app.services.address_service import AddressService
from app.schemas.addresses.response import AddressResponseSchema

bp = Blueprint("addresses", __name__, url_prefix="/api/addresses")

response_schema = AddressResponseSchema(many=True)
address_service = AddressService()


@bp.route("/", methods=["GET"])
def get_all_addresses():
    addresses = address_service.get_all()
    return jsonify(response_schema.dump(addresses)), 200

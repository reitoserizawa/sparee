import os
from mapbox import Geocoder
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from app.models.address import AddressStatus


class AddressJob:
    @staticmethod
    async def geocode_address_job(session: AsyncSession, address_id: int) -> None:
        from app import create_app
        from app.services.address_service import AddressService

        app = create_app()
        with app.app_context():
            address = await AddressService.get_or_raise(session, address_id)
            if not address:
                return

            api_key = os.getenv("MAPBOX_API_KEY")
            status = AddressStatus.FAILED
            if api_key:
                geocoder = Geocoder(access_token=api_key)
                query = address.full_address
                response = geocoder.forward(query)

                if response.status_code == 200:
                    geojson = response.json()
                    features = geojson.get("features", [])
                    if features:

                        lng, lat = features[0]["geometry"]["coordinates"]
                        address.location = from_shape(
                            Point(lng, lat), srid=4326)
                        status = AddressStatus.SUCCESS
            address.geocode_status = status
            await address.save(session)

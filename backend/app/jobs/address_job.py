import os
from mapbox import Geocoder
from geoalchemy2.shape import from_shape
from shapely.geometry import Point


class AddressJob:
    @staticmethod
    def geocode_address_job(address_id: int) -> None:
        from app import create_app
        from app.services.address_service import AddressService

        app = create_app()
        with app.app_context():
            address = AddressService.get_or_raise(address_id)
            if not address:
                return

            api_key = os.getenv("MAPBOX_API_KEY")
            if not api_key:
                address.geocode_status = "failed"
                address.save()
                return

            geocoder = Geocoder(access_token=api_key)

            query = address.full_address
            response = geocoder.forward(query)

            if response.status_code != 200:
                address.geocode_status = "failed"
                address.save()
                return

            geojson = response.json()
            features = geojson.get("features", [])
            print(features)
            if not features:
                address.geocode_status = "failed"
                address.save()
                return

            lng, lat = features[0]["geometry"]["coordinates"]
            address.location = from_shape(Point(lng, lat), srid=4326)
            address.save()

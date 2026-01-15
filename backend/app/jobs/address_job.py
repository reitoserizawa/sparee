import os
from mapbox import Geocoder
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

from app.models.address import Address


class AddressJob:
    @staticmethod
    def geocode_address_job(address: Address) -> None:
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
        if not features:
            address.geocode_status = "failed"
            address.save()
            return

        lng, lat = features[0]["geometry"]["coordinates"]
        address.location = from_shape(Point(lng, lat), srid=4326)
        address.save()

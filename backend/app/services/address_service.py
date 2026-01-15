import os
from mapbox import Geocoder
from app.models.address import Address


class AddressService:
    async def create_address(self, street: str, city: str, state: str, postal_code: str, country: str = "USA") -> Address:
        api_key = os.getenv("MAPBOX_API_KEY")

        if not api_key:
            raise EnvironmentError(
                "MAPBOX_API_KEY not set in environment variables")

        geocoder = Geocoder(access_token=api_key)
        address = f"{street}, {city}, {state}, {postal_code}, {country}"
        response = geocoder.forward(address)

        if response.status_code == 200:
            geojson = response.geojson()
            features = geojson.get('features', [])
            if features:
                first_result = features[0]
                coordinates = first_result['geometry']['coordinates']
                lng, lat = coordinates[0], coordinates[1]
        else:
            lng, lat = None, None

        address = Address(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            lat=lat,
            lng=lng,
        )
        address.save()
        return address

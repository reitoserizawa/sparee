import os
from shapely.geometry import Point
from geoalchemy2.shape import from_shape
from sqlalchemy.ext.asyncio import AsyncSession
from httpx import AsyncClient

from app.db.models.address import AddressStatus


class AddressJob:
    @staticmethod
    async def geocode_address_async(session: AsyncSession, address_id: int) -> None:
        from app.services.address_service import AddressService
        """Async version: uses async DB and async HTTP client."""
        address = await AddressService.get_or_raise(session, address_id)
        if not address:
            return

        api_key = os.getenv("MAPBOX_API_KEY")
        status = AddressStatus.failed

        if api_key:
            async with AsyncClient() as client:
                query = address.full_address
                response = await client.get(
                    f"https://api.mapbox.com/geocoding/v5/mapbox.places/{query}.json",
                    params={"access_token": api_key},
                    timeout=10
                )

                if response.status_code == 200:
                    geojson = response.json()
                    features = geojson.get("features", [])
                    if features:
                        lng, lat = features[0]["geometry"]["coordinates"]
                        address.location = from_shape(
                            Point(lng, lat), srid=4326)
                        status = AddressStatus.success

        address.geocode_status = status
        await address.save(session)

    @staticmethod
    def geocode_address_job(address_id: int):
        from app.db.session import AsyncSessionLocal

        async def _run():
            async with AsyncSessionLocal() as session:
                await AddressJob.geocode_address_async(session, address_id)

        return _run()

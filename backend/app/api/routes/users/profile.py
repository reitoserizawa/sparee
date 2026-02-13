from fastapi import APIRouter, Depends

from app.schemas.users import UserResponseModel
from app.api.dependencies.user_required import user_required
from app.db.models import User
from app.services.company_service import CompanyService

router = APIRouter()
company_service = CompanyService()


@router.get("", status_code=200, response_model=UserResponseModel)
async def profile(
    user: User = Depends(user_required),
):
    return user

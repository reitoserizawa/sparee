from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.user_required import user_required
from app.db.session import get_session
from app.db.models import User
from app.services.conversation_service import ConversationService
from app.schemas.conversations.response import ConversationResponseModel

router = APIRouter()
conversation_service = ConversationService()


@router.get("/", status_code=200, response_model=list[ConversationResponseModel])
async def get_user_conversations(
    session: AsyncSession = Depends(get_session),
    user: User = Depends(user_required),
):
    conversations = await conversation_service.get_from_user(
        session=session,
        user=user,
    )
    return conversations

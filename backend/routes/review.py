from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_db
from backend.models.models import User
from backend.routes.auth import get_current_user
from backend.services.spaced_repetition import get_due_reviews, review_card

router = APIRouter(prefix="/api/review", tags=["review"])


class ReviewRequest(BaseModel):
    topic_slug: str
    quality: int


@router.get("/due")
async def due_reviews(user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    reviews = await get_due_reviews(db, user.id)
    return {"reviews": reviews, "count": len(reviews)}


@router.post("/submit")
async def submit_review(req: ReviewRequest, user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    from backend.services.knowledge_service import get_topic_by_slug
    topic = await get_topic_by_slug(db, req.topic_slug)
    if not topic:
        return {"error": "Topic not found"}

    result = await review_card(db, user.id, topic.id, max(0, min(5, req.quality)))
    return result

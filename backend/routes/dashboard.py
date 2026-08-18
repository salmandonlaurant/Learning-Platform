from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_db
from backend.models.models import User
from backend.routes.auth import get_current_user
from backend.services.chapter_service import (
    get_all_chapters, get_overall_progress, get_user_book_progress,
    get_user_reading_progress,
)

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])


@router.get("")
async def get_dashboard(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    chapters = await get_all_chapters(db)
    progress = await get_overall_progress(db, user.id)
    bp = await get_user_book_progress(db, user.id)

    current_chapter = None
    if bp.current_chapter_id:
        ch_result = await get_user_reading_progress(db, user.id, bp.current_chapter_id)
        if ch_result:
            from backend.services.chapter_service import get_chapter_by_id
            ch = await get_chapter_by_id(db, bp.current_chapter_id)
            if ch:
                sections_done = len(ch_result.sections_read) if ch_result.sections_read else 0
                total_sections = len(ch.sections) if ch.sections else 0
                current_chapter = {
                    "id": ch.id,
                    "slug": ch.slug,
                    "title": ch.title,
                    "chapter_number": ch.chapter_number,
                    "category": ch.category,
                    "sections_read": sections_done,
                    "total_sections": total_sections,
                    "reading_percentage": round((sections_done / total_sections) * 100) if total_sections > 0 else 0,
                }

    recent_chapters = []
    for ch in chapters[:5]:
        rp = await get_user_reading_progress(db, user.id, ch.id)
        sections_done = len(rp.sections_read) if rp and rp.sections_read else 0
        total_sections = len(ch.sections) if ch.sections else 0
        recent_chapters.append({
            "id": ch.id,
            "slug": ch.slug,
            "title": ch.title,
            "chapter_number": ch.chapter_number,
            "category": ch.category,
            "sections_read": sections_done,
            "total_sections": total_sections,
            "quiz_passed": rp.quiz_passed if rp else None,
            "difficulty": ch.difficulty,
        })

    return {
        "user": {"id": user.id, "username": user.username},
        "progress": progress,
        "current_chapter": current_chapter,
        "recent_chapters": recent_chapters,
        "total_chapters": len(chapters),
    }

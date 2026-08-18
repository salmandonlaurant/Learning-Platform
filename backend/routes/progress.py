from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_db
from backend.models.models import User
from backend.routes.auth import get_current_user
from backend.services.chapter_service import (
    update_section_read, submit_quiz, update_reading_time,
    get_overall_progress, get_user_book_progress, get_user_reading_progress,
    get_all_chapters, get_chapter_by_id,
)

router = APIRouter(prefix="/api/progress", tags=["progress"])


class SectionReadRequest(BaseModel):
    chapter_id: int
    section_number: int


class QuizSubmitRequest(BaseModel):
    chapter_id: int
    answers: list[int]


class ReadingTimeRequest(BaseModel):
    seconds: int


@router.post("/section-read")
async def mark_section_read(
    req: SectionReadRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    rp = await update_section_read(db, user.id, req.chapter_id, req.section_number)
    return {"sections_read": rp.sections_read}


@router.post("/quiz-submit")
async def submit_quiz_result(
    req: QuizSubmitRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await submit_quiz(db, user.id, req.chapter_id, req.answers)
    if result is None:
        return {"error": "Chapter not found"}
    return result


@router.post("/reading-time")
async def add_reading_time(
    req: ReadingTimeRequest,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await update_reading_time(db, user.id, req.seconds)
    return {"ok": True}


@router.get("/overall")
async def get_progress_overview(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await get_overall_progress(db, user.id)


@router.get("/chapter/{chapter_id}")
async def get_chapter_progress(
    chapter_id: int,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    rp = await get_user_reading_progress(db, user.id, chapter_id)
    if not rp:
        return {
            "sections_read": [],
            "quiz_score": None,
            "quiz_total": None,
            "quiz_passed": None,
            "completed": False,
        }
    return {
        "sections_read": rp.sections_read or [],
        "quiz_score": rp.quiz_score,
        "quiz_total": rp.quiz_total,
        "quiz_passed": rp.quiz_passed,
        "completed": rp.completed_at is not None,
        "reading_time_seconds": rp.reading_time_seconds,
    }


@router.get("/book")
async def get_book_progress(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    bp = await get_user_book_progress(db, user.id)
    chapters = await get_all_chapters(db)

    chapter_progress = []
    for ch in chapters:
        rp = await get_user_reading_progress(db, user.id, ch.id)
        total_sections = len(ch.sections) if hasattr(ch, 'sections') and ch.sections else 0
        sections_done = len(rp.sections_read) if rp and rp.sections_read else 0
        chapter_progress.append({
            "chapter_id": ch.id,
            "slug": ch.slug,
            "title": ch.title,
            "part_number": ch.part_number,
            "chapter_number": ch.chapter_number,
            "sections_read": sections_done,
            "total_sections": total_sections,
            "quiz_passed": rp.quiz_passed if rp else None,
            "quiz_score": rp.quiz_score if rp else None,
            "quiz_total": rp.quiz_total if rp else None,
        })

    return {
        "chapters_completed": bp.chapters_completed,
        "daily_streak": bp.daily_streak,
        "total_reading_time_seconds": bp.total_reading_time_seconds,
        "current_chapter_id": bp.current_chapter_id,
        "chapter_progress": chapter_progress,
    }

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.database import get_db
from backend.models.models import User
from backend.routes.auth import get_current_user
from backend.services.chapter_service import (
    get_all_chapters, get_chapter_by_slug, get_chapter_by_id,
    get_user_book_progress, get_user_reading_progress,
)

router = APIRouter(prefix="/api/chapters", tags=["chapters"])


@router.get("")
async def list_chapters(db: AsyncSession = Depends(get_db)):
    chapters = await get_all_chapters(db)
    return [
        {
            "id": c.id,
            "slug": c.slug,
            "title": c.title,
            "subtitle": c.subtitle,
            "category": c.category,
            "part_number": c.part_number,
            "chapter_number": c.chapter_number,
            "difficulty": c.difficulty,
            "estimated_minutes": c.estimated_minutes,
            "intro_hook": c.intro_hook,
            "key_takeaways": c.key_takeaways,
        }
        for c in chapters
    ]


@router.get("/parts")
async def list_parts(db: AsyncSession = Depends(get_db)):
    chapters = await get_all_chapters(db)
    parts = {}
    for c in chapters:
        pn = c.part_number
        if pn not in parts:
            parts[pn] = {
                "part_number": pn,
                "title": c.category.split(": ", 1)[1] if ": " in c.category else c.category,
                "chapters": [],
            }
        parts[pn]["chapters"].append({
            "id": c.id,
            "slug": c.slug,
            "title": c.title,
            "chapter_number": c.chapter_number,
            "estimated_minutes": c.estimated_minutes,
            "difficulty": c.difficulty,
        })
    return list(parts.values())


@router.get("/{slug}")
async def get_chapter(
    slug: str,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    chapter = await get_chapter_by_slug(db, slug)
    if not chapter:
        return {"error": "Chapter not found"}

    reading_progress = await get_user_reading_progress(db, user.id, chapter.id)
    sections_read = reading_progress.sections_read if reading_progress else []

    return {
        "id": chapter.id,
        "slug": chapter.slug,
        "title": chapter.title,
        "subtitle": chapter.subtitle,
        "category": chapter.category,
        "part_number": chapter.part_number,
        "chapter_number": chapter.chapter_number,
        "difficulty": chapter.difficulty,
        "estimated_minutes": chapter.estimated_minutes,
        "intro_hook": chapter.intro_hook,
        "key_takeaways": chapter.key_takeaways,
        "vocabulary": chapter.vocabulary_json,
        "sections": [
            {
                "section_number": s.section_number,
                "title": s.title,
                "content": s.content,
                "read": s.section_number in sections_read,
            }
            for s in chapter.sections
        ],
        "quiz_questions": len(chapter.quizzes),
        "reading_progress": {
            "sections_read": sections_read,
            "total_sections": len(chapter.sections),
        },
    }


@router.get("/{slug}/quiz")
async def get_chapter_quiz(
    slug: str,
    db: AsyncSession = Depends(get_db),
):
    chapter = await get_chapter_by_slug(db, slug)
    if not chapter:
        return {"error": "Chapter not found"}

    return {
        "chapter_id": chapter.id,
        "chapter_title": chapter.title,
        "questions": [
            {
                "question_number": q.question_number,
                "question_text": q.question_text,
                "options": q.options_json,
            }
            for q in chapter.quizzes
        ],
    }


def _part_title(num: int) -> str:
    titles = {
        1: "Foundations",
        2: "Attacks & Defenses",
        3: "Advanced Topics",
    }
    return titles.get(num, f"Part {num}")

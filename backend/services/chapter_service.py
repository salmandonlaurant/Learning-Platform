from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
import datetime

from backend.models.models import (
    Chapter, ChapterSection, ChapterQuiz,
    ReadingProgress, UserBookProgress, User
)
from backend.services.chapters_data import CHAPTERS_DATA
from backend.services.chapters_data_part2 import CHAPTERS_DATA_PART2
from backend.services.chapters_data_part3 import CHAPTERS_DATA_PART3


ALL_CHAPTERS = CHAPTERS_DATA + CHAPTERS_DATA_PART2 + CHAPTERS_DATA_PART3


async def seed_chapters(db: AsyncSession):
    result = await db.execute(select(func.count(Chapter.id)))
    if result.scalar() > 0:
        return

    for ch_data in ALL_CHAPTERS:
        chapter = Chapter(
            slug=ch_data["slug"],
            title=ch_data["title"],
            subtitle=ch_data.get("subtitle", ""),
            category=ch_data["category"],
            part_number=ch_data["part_number"],
            chapter_number=ch_data["chapter_number"],
            difficulty=ch_data.get("difficulty", "beginner"),
            estimated_minutes=ch_data.get("estimated_minutes", 25),
            intro_hook=ch_data.get("intro_hook", ""),
            key_takeaways=ch_data.get("key_takeaways", []),
            vocabulary_json=ch_data.get("vocabulary_json", []),
        )
        db.add(chapter)
        await db.flush()

        for i, sec in enumerate(ch_data.get("sections", [])):
            section = ChapterSection(
                chapter_id=chapter.id,
                section_number=i + 1,
                title=sec["title"],
                content=sec["content"],
            )
            db.add(section)

        for q in ch_data.get("quizzes", []):
            quiz = ChapterQuiz(
                chapter_id=chapter.id,
                question_number=q["question_number"],
                question_type=q.get("question_type", "multiple_choice"),
                question_text=q["question_text"],
                options_json=q.get("options_json") or q.get("options", []),
                correct_index=q["correct_index"],
                explanation=q.get("explanation", ""),
            )
            db.add(quiz)

    await db.commit()


async def get_all_chapters(db: AsyncSession):
    result = await db.execute(
        select(Chapter)
        .options(selectinload(Chapter.sections))
        .where(Chapter.is_published == True)
        .order_by(Chapter.part_number, Chapter.chapter_number)
    )
    return result.scalars().unique().all()


async def get_chapter_by_slug(db: AsyncSession, slug: str):
    result = await db.execute(
        select(Chapter)
        .options(selectinload(Chapter.sections), selectinload(Chapter.quizzes))
        .where(Chapter.slug == slug)
    )
    return result.scalars().first()


async def get_chapter_by_id(db: AsyncSession, chapter_id: int):
    result = await db.execute(
        select(Chapter)
        .options(selectinload(Chapter.sections), selectinload(Chapter.quizzes))
        .where(Chapter.id == chapter_id)
    )
    return result.scalars().first()


async def get_user_book_progress(db: AsyncSession, user_id: int):
    result = await db.execute(
        select(UserBookProgress).where(UserBookProgress.user_id == user_id)
    )
    progress = result.scalars().first()
    if not progress:
        progress = UserBookProgress(user_id=user_id)
        db.add(progress)
        await db.commit()
        await db.refresh(progress)
    return progress


async def get_user_reading_progress(db: AsyncSession, user_id: int, chapter_id: int):
    result = await db.execute(
        select(ReadingProgress).where(
            ReadingProgress.user_id == user_id,
            ReadingProgress.chapter_id == chapter_id,
        )
    )
    return result.scalars().first()


async def update_section_read(db: AsyncSession, user_id: int, chapter_id: int, section_number: int):
    rp = await get_user_reading_progress(db, user_id, chapter_id)
    if not rp:
        rp = ReadingProgress(user_id=user_id, chapter_id=chapter_id, sections_read=[])
        db.add(rp)

    sections_read = rp.sections_read or []
    if section_number not in sections_read:
        sections_read.append(section_number)
        sections_read.sort()
        rp.sections_read = sections_read

    await db.commit()
    await db.refresh(rp)
    return rp


async def submit_quiz(db: AsyncSession, user_id: int, chapter_id: int, answers: list[int]):
    chapter = await get_chapter_by_id(db, chapter_id)
    if not chapter:
        return None

    quizzes = sorted(chapter.quizzes, key=lambda q: q.question_number)
    correct = 0
    results = []

    for i, quiz in enumerate(quizzes):
        user_answer = answers[i] if i < len(answers) else -1
        is_correct = user_answer == quiz.correct_index
        if is_correct:
            correct += 1
        results.append({
            "question_number": quiz.question_number,
            "question_text": quiz.question_text,
            "user_answer": user_answer,
            "correct_answer": quiz.correct_index,
            "is_correct": is_correct,
            "explanation": quiz.explanation,
        })

    total = len(quizzes)
    score_pct = round((correct / total) * 100) if total > 0 else 0
    passed = score_pct >= 60

    rp = await get_user_reading_progress(db, user_id, chapter_id)
    if not rp:
        rp = ReadingProgress(user_id=user_id, chapter_id=chapter_id, sections_read=[])
        db.add(rp)

    rp.quiz_score = correct
    rp.quiz_total = total
    rp.quiz_passed = passed
    if passed:
        rp.completed_at = datetime.datetime.utcnow()

    await db.commit()

    bp = await get_user_book_progress(db, user_id)
    completed_count = await db.execute(
        select(func.count(ReadingProgress.id)).where(
            ReadingProgress.user_id == user_id,
            ReadingProgress.quiz_passed == True,
        )
    )
    bp.chapters_completed = completed_count.scalar() or 0
    if passed and bp.current_chapter_id == chapter_id:
        next_ch = await db.execute(
            select(Chapter)
            .where(Chapter.chapter_number == chapter.chapter_number + 1)
            .where(Chapter.is_published == True)
        )
        next_chapter = next_ch.scalars().first()
        if next_chapter:
            bp.current_chapter_id = next_chapter.id
    await db.commit()

    return {
        "score": correct,
        "total": total,
        "score_percentage": score_pct,
        "passed": passed,
        "results": results,
    }


async def update_reading_time(db: AsyncSession, user_id: int, seconds: int):
    bp = await get_user_book_progress(db, user_id)
    bp.total_reading_time_seconds += seconds

    today = datetime.date.today().isoformat()
    if bp.last_reading_date == today:
        pass
    elif bp.last_reading_date:
        last = datetime.date.fromisoformat(bp.last_reading_date)
        diff = (datetime.date.today() - last).days
        if diff == 1:
            bp.daily_streak += 1
        elif diff > 1:
            bp.daily_streak = 1
    else:
        bp.daily_streak = 1

    bp.last_reading_date = today
    await db.commit()


async def get_overall_progress(db: AsyncSession, user_id: int):
    total = await db.execute(select(func.count(Chapter.id)).where(Chapter.is_published == True))
    total_chapters = total.scalar() or 0

    completed = await db.execute(
        select(func.count(ReadingProgress.id)).where(
            ReadingProgress.user_id == user_id,
            ReadingProgress.quiz_passed == True,
        )
    )
    completed_chapters = completed.scalar() or 0

    bp = await get_user_book_progress(db, user_id)

    return {
        "total_chapters": total_chapters,
        "completed_chapters": completed_chapters,
        "percentage": round((completed_chapters / total_chapters) * 100) if total_chapters > 0 else 0,
        "daily_streak": bp.daily_streak,
        "total_reading_time_seconds": bp.total_reading_time_seconds,
        "current_chapter_id": bp.current_chapter_id,
    }

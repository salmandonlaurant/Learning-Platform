import math
from datetime import datetime, timedelta

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.models import SpacedRepetitionCard, Topic, UserTopicConfidence


async def get_or_create_card(db: AsyncSession, user_id: int, topic_id: int) -> SpacedRepetitionCard:
    result = await db.execute(
        select(SpacedRepetitionCard).where(
            SpacedRepetitionCard.user_id == user_id,
            SpacedRepetitionCard.topic_id == topic_id,
        )
    )
    card = result.scalars().first()
    if card:
        return card

    card = SpacedRepetitionCard(
        user_id=user_id,
        topic_id=topic_id,
        ease_factor=2.5,
        interval_days=1,
        repetitions=0,
        next_review=datetime.utcnow() + timedelta(days=1),
        last_review=None,
        performance_json=[],
    )
    db.add(card)
    await db.flush()
    return card


def calculate_next_review(card: SpacedRepetitionCard, quality: int) -> dict:
    """Calculate next review based on SM-2 algorithm.

    quality: 0-5 (0-2: failed, 3: hard, 4: good, 5: easy)
    """
    performance = card.performance_json or []
    performance.append(quality)

    if quality < 3:
        card.repetitions = 0
        card.interval_days = 1
    else:
        if card.repetitions == 0:
            card.interval_days = 1
        elif card.repetitions == 1:
            card.interval_days = 3
        else:
            card.interval_days = round(card.interval_days * card.ease_factor)
        card.repetitions += 1

    card.ease_factor = max(1.3, card.ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))

    if quality < 3:
        card.ease_factor = max(1.3, card.ease_factor - 0.2)

    card.next_review = datetime.utcnow() + timedelta(days=card.interval_days)
    card.last_review = datetime.utcnow()
    card.performance_json = performance[-20:]

    return {
        "next_review": card.next_review.isoformat(),
        "interval_days": card.interval_days,
        "ease_factor": round(card.ease_factor, 2),
        "repetitions": card.repetitions,
    }


async def review_card(db: AsyncSession, user_id: int, topic_id: int, quality: int) -> dict:
    card = await get_or_create_card(db, user_id, topic_id)
    result = calculate_next_review(card, quality)

    conf_result = await db.execute(
        select(UserTopicConfidence).where(
            UserTopicConfidence.user_id == user_id,
            UserTopicConfidence.topic_id == topic_id,
        )
    )
    conf = conf_result.scalars().first()
    if conf:
        conf.times_quizzed += 1
        if quality >= 3:
            conf.times_correct += 1
        accuracy = conf.times_correct / conf.times_quizzed if conf.times_quizzed > 0 else 0
        conf.confidence = min(1.0, accuracy * min(1.0, conf.times_quizzed / 5))
        conf.last_reviewed = datetime.utcnow()

        if conf.confidence >= 0.8:
            conf.status = "mastered"
        elif conf.confidence >= 0.5:
            conf.status = "learning"
        elif conf.times_quizzed > 0:
            conf.status = "weak"
        else:
            conf.status = "new"

    await db.commit()
    return result


async def get_due_reviews(db: AsyncSession, user_id: int, limit: int = 10) -> list:
    now = datetime.utcnow()
    result = await db.execute(
        select(SpacedRepetitionCard)
        .where(
            SpacedRepetitionCard.user_id == user_id,
            SpacedRepetitionCard.next_review <= now,
        )
        .order_by(SpacedRepetitionCard.next_review)
        .limit(limit)
    )
    cards = result.scalars().all()

    topics = []
    for card in cards:
        topic_result = await db.execute(select(Topic).where(Topic.id == card.topic_id))
        topic = topic_result.scalars().first()
        if topic:
            topics.append({
                "card_id": card.id,
                "topic": topic.name,
                "slug": topic.slug,
                "interval_days": card.interval_days,
                "repetitions": card.repetitions,
                "next_review": card.next_review.isoformat(),
            })

    return topics

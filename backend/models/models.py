import datetime
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey, JSON
)
from sqlalchemy.orm import relationship

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    book_progress = relationship("UserBookProgress", back_populates="user", uselist=False)
    reading_progress = relationship("ReadingProgress", back_populates="user")


class UserBookProgress(Base):
    __tablename__ = "user_book_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    current_chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=True)
    chapters_completed = Column(Integer, default=0)
    total_reading_time_seconds = Column(Integer, default=0)
    daily_streak = Column(Integer, default=0)
    last_reading_date = Column(String(10), nullable=True)

    user = relationship("User", back_populates="book_progress")
    current_chapter = relationship("Chapter", foreign_keys=[current_chapter_id])


class Chapter(Base):
    __tablename__ = "chapters"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(200), unique=True, nullable=False, index=True)
    title = Column(String(300), nullable=False)
    subtitle = Column(String(500), default="")
    category = Column(String(100), nullable=False, index=True)
    part_number = Column(Integer, nullable=False)
    chapter_number = Column(Integer, nullable=False)
    difficulty = Column(String(20), default="beginner")
    estimated_minutes = Column(Integer, default=25)
    intro_hook = Column(Text, default="")
    key_takeaways = Column(JSON, default=list)
    vocabulary_json = Column(JSON, default=list)
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    sections = relationship("ChapterSection", back_populates="chapter", order_by="ChapterSection.section_number")
    quizzes = relationship("ChapterQuiz", back_populates="chapter", order_by="ChapterQuiz.question_number")
    reading_progress = relationship("ReadingProgress", back_populates="chapter")


class ChapterSection(Base):
    __tablename__ = "chapter_sections"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    section_number = Column(Integer, nullable=False)
    title = Column(String(300), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    chapter = relationship("Chapter", back_populates="sections")


class ChapterQuiz(Base):
    __tablename__ = "chapter_quizzes"

    id = Column(Integer, primary_key=True, index=True)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    question_number = Column(Integer, nullable=False)
    question_type = Column(String(30), default="multiple_choice")
    question_text = Column(Text, nullable=False)
    options_json = Column(JSON, nullable=False)
    correct_index = Column(Integer, nullable=False)
    explanation = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    chapter = relationship("Chapter", back_populates="quizzes")


class ReadingProgress(Base):
    __tablename__ = "reading_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    chapter_id = Column(Integer, ForeignKey("chapters.id"), nullable=False)
    sections_read = Column(JSON, default=list)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    quiz_score = Column(Integer, nullable=True)
    quiz_total = Column(Integer, nullable=True)
    quiz_passed = Column(Boolean, nullable=True)
    reading_time_seconds = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="reading_progress")
    chapter = relationship("Chapter", back_populates="reading_progress")

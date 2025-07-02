# app/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Index
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, UTC

Base = declarative_base()  # 👈 Move it here

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    content = Column(Text)
    rating = Column(Integer)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

    book = relationship("Book", back_populates="reviews")

    __table_args__ = (
        Index('ix_reviews_book_id', "book_id"),
    )

# this file defines the database models for the application.
# It uses SQLAlchemy's declarative base to define the structure of the database tables.
# It includes two models: Book and Review, with their respective fields and relationships.
# The Book model represents a book with fields for title, author, and creation date.
# The Review model represents a review for a book, with fields for content, rating, and creation date.
# The Review model has a foreign key relationship with the Book model, allowing for easy retrieval of reviews associated with a specific book.
# It also includes an index on the book_id field in the Review model for efficient querying.

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Index
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, UTC

Base = declarative_base()  

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

# DB operations (Create, Read)

# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def create_book(db: Session, book_data: schemas.BookCreate):
    new_book = models.Book(**book_data.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_books(db: Session):
    return db.query(models.Book).all()


def create_review(db: Session, book_id: int, review: schemas.ReviewCreate):
    db_review = models.Review(**review.model_dump(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_reviews_for_book(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()


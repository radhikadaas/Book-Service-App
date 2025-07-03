# DB operations (Create, Read) for books and reviews
from sqlalchemy.orm import Session
from app import models, schemas

# Function to create a new book in the database
# This function takes a database session and a BookCreate schema as input
def create_book(db: Session, book_data: schemas.BookCreate):
    new_book = models.Book(**book_data.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

## Function to retrieve all books from the database
# This function queries the database for all Book records and returns them as a list.
def get_books(db: Session):
    return db.query(models.Book).all()

## Function to retrieve a book by its ID
# This function queries the database for a specific Book record by its ID.
def create_review(db: Session, book_id: int, review: schemas.ReviewCreate):
    db_review = models.Review(**review.model_dump(), book_id=book_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

# Function to retrieve all reviews for a specific book
# This function queries the database for all Review records associated with a specific book ID.
def get_reviews_for_book(db: Session, book_id: int):
    return db.query(models.Review).filter(models.Review.book_id == book_id).all()


# /reviews endpoints

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db import get_db

router = APIRouter()

@router.post("/books/{book_id}/reviews", response_model=schemas.ReviewResponse, status_code=201)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, book_id, review)


@router.get("/books/{book_id}/reviews", response_model=list[schemas.ReviewResponse])
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_for_book(db, book_id)

# /books endpoints
# app/routers/books.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db import get_db
from app.cache import get_cached_books, set_cached_books
import asyncio


router = APIRouter()

@router.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/books", response_model=list[schemas.BookResponse])
async def read_books(db: Session = Depends(get_db)):
    cached = await get_cached_books()
    if cached:
        return cached

    books = crud.get_books(db)
    result = [schemas.BookResponse.model_validate(b).model_dump() for b in books]
    await set_cached_books(result)
    return result
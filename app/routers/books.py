# /books endpoints
# app/routers/books.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.db import get_db
from app.cache import get_cached_books, set_cached_books
import asyncio


router = APIRouter()

# This endpoint is used to create a new book in the database.
# It accepts a BookCreate schema as input and returns the created book.
# The book is created using the CRUD operations defined in the app.crud module.
# The response is a BookResponse schema.
@router.post("/books", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

# This endpoint is used to retrieve all books from the database.
# If the books are cached, it returns the cached data.
# If not, it fetches from the database, caches the result, and returns it.
# It uses async functions to handle caching operations, allowing for non-blocking I/O.
@router.get("/books", response_model=list[schemas.BookResponse])
async def read_books(db: Session = Depends(get_db)):
    cached = await get_cached_books() # why awiat -- because it is an async function 
    if cached:
        return cached

    books = crud.get_books(db)
    result = [schemas.BookResponse.model_validate(b).model_dump() for b in books]
    await set_cached_books(result)
    return result
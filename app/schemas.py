# Pydantic schemas for validation
#  input/output validation --> kya bejna hai, kya lena hai
# app/schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: Optional[str] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True



# app/schemas.py

class ReviewCreate(BaseModel):
    content: str
    rating: int

class ReviewResponse(BaseModel):
    id: int
    book_id: int
    content: str
    rating: int
    created_at: datetime

    class Config:
        from_attributes = True

# FastAPI app starts here

# app/main.py
from fastapi import FastAPI
from app.routers import books, reviews
from app import models
from app.db import engine


app = FastAPI()

# Optional: create tables if not using Alembic
# models.Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(books.router) # --> routers/books wali file me se saare router import kiya hai
app.include_router(reviews.router) # -> routers/reviews wali file me se saare router import kiya hai

# Root route
@app.get("/")
def read_root():
    return {"message": "📚 Book Review API is Live!"}

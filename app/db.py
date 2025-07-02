 # DB connection setup

# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from app.models import Base # ✅ Forces models to load into Base metadata
from typing import cast

# Load environment variables from .env
load_dotenv()

DATABASE_URL = cast(str, os.getenv("DATABASE_URL"))

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

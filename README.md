# 📚 Book Review API

A lightweight microservice for managing books and their reviews. Built using **FastAPI**, **PostgreSQL**, **Redis**, and **SQLAlchemy** with full test coverage and database migration support.

---

## 🔗 Repository

[GitHub – Book Review API](hhttps://github.com/radhikadaas/Book-Service-App)

---

## 🚀 Features

- Add and retrieve books with metadata
- Add and fetch reviews for specific books
- Redis caching for faster repeated queries
- Alembic migrations for schema changes
- Unit and integration tests with Pytest

---

## ⚙️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- Alembic
- Pytest

---

## 🧪 Running Locally

### ✅ Requirements

- Python 3.10+
- PostgreSQL 14+
- Redis 5+
- pipenv or venv

### 🔧 Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/book-review-service.git
cd book-review-service

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
````

### 🌍 Environment Variables

Create a `.env` file in the root:

```env
DATABASE_URL=postgresql://postgres:<password>@localhost:5432/book_review_db
REDIS_URL=redis://localhost:6379/0
REDIS_HOST=localhost
REDIS_PORT=6379
```

### 🛠️ Database Migration

```bash
alembic upgrade head
```

### 🚀 Start Server

```bash
uvicorn app.main:app --reload
```

Access docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ Running Tests

```bash
pytest tests/test_books.py
pytest tests/test_cache.py
```

---

## 🧭 API Endpoints

| Method | Endpoint              | Description                     |
| ------ | --------------------- | ------------------------------- |
| GET    | `/books`              | List all books                  |
| POST   | `/books`              | Add a new book                  |
| GET    | `/books/{id}/reviews` | Get reviews for a specific book |
| POST   | `/books/{id}/reviews` | Add a review to a book          |

---

## 🧱 Project Structure

```txt
app/
├── main.py            # FastAPI entry point
├── models.py          # SQLAlchemy models
├── db.py              # DB connection setup
├── crud.py            # DB operations
├── schemas.py         # Pydantic models
├── cache.py           # Redis logic
└── routers/
    ├── books.py
    └── reviews.py

alembic/
├── env.py
└── versions/          # Migration files

tests/
├── test_books.py
└── test_cache.py
```

---

## 🔄 Architecture Overview
- Paste the code into [Mermaid](https://mermaid.js.org/) for flow diagram
```bash
flowchart TD
 subgraph Routers["Routers"]
        D1["routers/books.py"]
        D2["routers/reviews.py"]
  end
 subgraph DataAccess["DataAccess"]
        crud["CRUD Functions"]
        schemas["Pydantic Schemas"]
        db["db.py - Session & Engine"]
        models["SQLAlchemy Models"]
  end
    A@{ label: "Start: Run `main.py`" } --> B["FastAPI app created"]
    B --> C["Include routers"]
    C --> D1 & D2
    D1 --> E1["GET /books or POST /books"]
    E1 --> F1{"Check Redis Cache?"} & J1["Validate with BookCreate schema"]
    F1 -- Yes --> G1["Return Cached Books"]
    F1 -- No --> H1["Call CRUD to fetch books from DB"]
    H1 --> I1["Set books in Redis Cache"]
    I1 --> G1 & cache["cache.py"]
    J1 --> K1["Call crud.create_book"] & schemas
    K1 --> L1["Insert into DB using SQLAlchemy"] & crud
    L1 --> M1["Return BookResponse schema"]
    D2 --> E2["Access /books/:id/reviews endpoints"]
    E2 --> J2["Validate with ReviewCreate schema"] & N2["Call crud.get_reviews_by_book_id"]
    J2 --> K2["Call crud.create_review"] & schemas
    K2 --> L2["Insert review into DB"] & crud
    L2 --> M2["Return ReviewResponse schema"]
    N2 --> O2["Return list of reviews"] & crud
    crud --> db & models
    M1 --> schemas
    M2 --> schemas
    models --> DB[("PostgreSQL Database")]
    cache --> Redis[("Redis Cache")]
    F1 --> cache
    T1["test_books.py"] --> D1
    T2["test_cache.py"] --> cache
    A@{ shape: rect}

```

---

## 📬 Contact

Made by [@radhikadaas](https://github.com/radhikadaas)
Open an issue or PR for questions, feedback, or contributions.

---

## 🌟 Notes

* Redis speeds up repeated `GET` requests
* Full test coverage with Pytest
* Ready for features like user auth and ratings

---

## Full Documentaion
- Docs - [Docs](https://docs.google.com/document/d/1Ppt5HdhlHlG0Z88yo7l-QH4slE6k2QJjiHOa2N5zGfE/edit?usp=sharing)

> Made with ❤️ using FastAPI, PostgreSQL, and Redis

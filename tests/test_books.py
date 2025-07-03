import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


@pytest.fixture(scope="module")
def created_book_id():
    """Fixture to create a book once and share its ID"""
    payload = {
        "title": "Test Driven Dev",
        "author": "TDD Expert"
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 201  # Make sure your FastAPI endpoint returns 201
    return response.json()["id"]


def test_get_books():
    """Test GET /books endpoint - should return list of books"""
    response = client.get("/books")
    assert response.status_code == 200
    books = response.json()
    assert isinstance(books, list)
    if books:
        assert "title" in books[0]
        assert "author" in books[0]


def test_post_review_for_book(created_book_id):
    """Test POST /books/{book_id}/reviews - should add a review"""
    review_payload = {
        "content": "Awesome read!",
        "rating": 5
    }
    response = client.post(f"/books/{created_book_id}/reviews", json=review_payload)
    assert response.status_code == 201
    data = response.json()
    assert data["content"] == review_payload["content"]
    assert data["rating"] == review_payload["rating"]
    assert data["book_id"] == created_book_id


def test_get_reviews_for_book(created_book_id):
    """Test GET /books/{book_id}/reviews - should list reviews"""
    response = client.get(f"/books/{created_book_id}/reviews")
    assert response.status_code == 200
    reviews = response.json()
    assert isinstance(reviews, list)
    assert len(reviews) > 0
    assert reviews[0]["book_id"] == created_book_id

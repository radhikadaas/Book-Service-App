import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import redis.asyncio as redis
import json


@pytest.mark.asyncio
async def test_books_cache_miss():
    # Connect to Redis and clear the "books" key (simulate cache-miss)
    redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)
    await redis_client.delete("books")
    assert await redis_client.get("books") is None  # ✅ Confirm key is gone

    # Use ASGITransport to test FastAPI without starting a real server
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get("/books")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # Redis should now be populated
    cached = await redis_client.get("books")
    assert cached is not None
    assert isinstance(json.loads(cached), list)

    await redis_client.aclose()

# app/cache.py

import redis.asyncio as redis  # ✅ the async version
import json
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# ✅ Custom encoder to handle datetime
def default_json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

async def get_cached_books():
    try:
        books_json = await redis_client.get("books")  # ✅ await it
        if books_json:
            print("✅ Fetched from Redis cache")
            return json.loads(books_json)
    except Exception as e:
        print("⚠️ Redis error (get):", str(e))  # Logging only
    return None

async def set_cached_books(data):
    try:
        await redis_client.set("books", json.dumps(data, default=default_json_serializer), ex=60)

        print("📦 Stored in Redis cache")
    except Exception as e:
        print("⚠️ Redis error (set):", e)

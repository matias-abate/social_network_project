import redis
import os

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def set_cache(key, value, ttl=300):
    redis_client.setex(key, ttl, value)

def get_cache(key):
    return redis_client.get(key)
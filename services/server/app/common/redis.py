import os
from redis.asyncio.client import ConnectionPool
from redis.asyncio.client import Redis as RedisClient
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError
from redis.retry import Retry
from utils.logger import logger


class Redis:
    redis: RedisClient

    def __init__(self, username: str, password: str, domain: str, port: int):
        logger.info(f"Connecting to redis: {username}:{password}@{domain}:{port}")
        self.redis = RedisClient(
            connection_pool=ConnectionPool(
                host=domain,
                port=port,
                # password=password,
                username=username if username != "redis" else "",
                socket_keepalive=True,
                retry=Retry(ExponentialBackoff(), 3),
                retry_on_timeout=True,
                retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError],
                health_check_interval=30,
            )
        )
        logger.info("Redis connected")

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, *args, **kwargs):
        return await self.redis.set(*args, **kwargs)

    async def expire(self, *args, **kwargs):
        return await self.redis.expire(*args, **kwargs)

    async def close(self):
        if self.redis is not None:
            await self.redis.close()

    async def ping(self):
        return await self.redis.ping()


REDIS_USERNAME = os.environ.get("REDIS_USER")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")
REDIS_DOMAIN = os.environ.get("REDIS_DOMAIN")
REDIS_PORT = os.environ.get("REDIS_PORT")

redis = Redis(REDIS_USERNAME, REDIS_PASSWORD, REDIS_DOMAIN, REDIS_PORT)


async def close_redis(_app) -> None:
    await redis.close()


async def ping_redis(_app) -> None:
    await redis.ping()

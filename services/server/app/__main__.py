import os

from aiohttp import web
from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage
from aiohttp_swagger import setup_swagger
from common.consts import USER_SESSION_COOKIE_NAME
from common.middlewares.debug import json_payload_logger
from common.middlewares.error import common_errors
from common.redis import close_redis, ping_redis
from common.redis import redis as redis_client
from db import YOYO_CONN_STR, close_pg_pool, open_pg_pool
from modules.message.http import message_routes
from modules.user.http import user_routes
from modules.file.http import file_routes
from utils.logger import logger
from utils.swagger import definitions
from yoyo import get_backend, read_migrations

backend = get_backend(YOYO_CONN_STR)
migrations = read_migrations("app/migrations")

with backend.lock():
    migrations_to_apply = backend.to_apply(migrations)

    if len(migrations_to_apply) != 0:
        logger.info("Start postgres migrations")

        try:
            backend.apply_migrations(migrations_to_apply)
        except Exception as ex:
            logger.error("Failed postgres migration: %s", ex)
            exit(1)
        else:
            logger.info("Complete postgres migrations")

middlewares = [common_errors]

environment = os.environ.get("app_env_type", "development")

if environment == "development":
    middlewares.append(json_payload_logger)

app = web.Application(logger=logger, middlewares=middlewares)

app.on_startup.append(ping_redis)
app.on_startup.append(open_pg_pool)

app.on_cleanup.append(close_redis)
app.on_cleanup.append(close_pg_pool)

redis_storage = RedisStorage(redis_client.redis, cookie_name=USER_SESSION_COOKIE_NAME)
setup_session(app, redis_storage)

routes = user_routes + message_routes + file_routes

app.add_routes(routes)

setup_swagger(
    app,
    api_version="1.0",
    title="vsnder-api",
    swagger_url="/swagger",
    ui_version=3,
    swagger_validator_url="//online.swagger.io/validator",
    definitions=definitions,
)

if __name__ == "__main__":
    logger.info("Server started")

    web.run_app(app, port=int(os.environ.get("SERVER_PORT", 3000)))

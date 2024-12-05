import os
from db import open_pg_pool, close_pg_pool
from utils.logger import logger
from aiohttp import web
from aiohttp_session import setup as setup_session
from aiohttp_session.redis_storage import RedisStorage
from aiohttp_swagger import setup_swagger
from common.consts import USER_SESSION_COOKIE_NAME
from common.redis import redis as redis_client, close_redis, ping_redis

from modules.user.http import user_routes
from modules.message.http import message_routes
from common.middlewares.debug import json_payload_logger
from common.middlewares.error import common_errors
from utils.swagger import definitions

middlewares = [
    common_errors
]

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

routes = user_routes + message_routes

app.add_routes(routes)

setup_swagger(
    app,
    api_version="1.0",
    title="vsnder-api",
    swagger_url="/swagger",
    ui_version=3,
    swagger_validator_url="//online.swagger.io/validator",
    definitions=definitions
)

if __name__ == "__main__":
    logger.info("Server started")
    
    web.run_app(app, port=int(os.environ.get("SERVER_PORT", 3000)))

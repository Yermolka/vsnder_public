from asyncio import TimeoutError as AsyncTimeoutError
from pprint import pformat
from traceback import format_exception
from typing import Callable

from aiohttp.web import middleware
from aiohttp.web_exceptions import (
    HTTPClientError,
    HTTPInternalServerError,
    HTTPRequestTimeout,
    HTTPServerError,
    HTTPServiceUnavailable,
    HTTPTooManyRequests,
)
from aiohttp.web_request import Request
from utils.logger import logger
from psycopg.errors import OperationalError
from redis.exceptions import ConnectionError as RedisConnectionError
from redis.exceptions import TimeoutError as RedisTimeoutError


def format_ex(ex: BaseException):
    return "".join(format_exception(ex))


@middleware
async def common_errors(request: Request, handler: Callable):
    try:
        return await handler(request)
    except ConnectionResetError:
        pass
    except HTTPClientError as ex:
        logger.debug(f"request: {pformat(request)}, exception: {ex}, msg: {ex.text}")
        raise ex
    except HTTPServerError as ex:
        logger.error(f"request: {pformat(request)}, exception: {ex}, msg: {ex.text}")
        raise ex
    except RedisConnectionError as ex:
        logger.critical(format_ex(ex))
        raise HTTPServiceUnavailable
    except (OperationalError, RedisTimeoutError) as ex:
        logger.error(format_ex(ex))
        raise HTTPTooManyRequests
    except (TimeoutError, AsyncTimeoutError):
        raise HTTPRequestTimeout
    except Exception as ex:
        logger.error(format_ex(ex))
        raise HTTPInternalServerError(text=str(ex))

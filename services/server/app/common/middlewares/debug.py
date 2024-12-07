from pprint import pformat
from typing import Callable

from aiohttp.web import middleware
from aiohttp.web_request import Request
from utils.logger import logger


@middleware
async def json_payload_logger(request: Request, handler: Callable):
    if request.content_type == "application/json":
        try:
            body_data: dict = await request.json()
            logger.debug(f"Handler: {handler.__name__}, {pformat(body_data)}")
        except Exception:
            pass

    return await handler(request)

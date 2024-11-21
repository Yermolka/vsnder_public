from aiohttp.web import Request
from aiohttp.web_exceptions import HTTPUnauthorized
from functools import wraps
from typing import Callable
from hashlib import sha256

from aiohttp_session import get_session

from common.consts import PASSWORD_HASH_SALT


def get_password_hash(password: str):
    m = sha256()
    m.update(password.encode("utf-8"))
    m.update(PASSWORD_HASH_SALT)
    return m.hexdigest()


def check_password_match(password: str, password_hash: str):
    return get_password_hash(password) == password_hash


def auth_guard():
    def _auth_guard(handler: Callable):
        @wraps(handler)
        async def wrapper(*args, **kwargs):
            request: Request = args[0]
            session = await get_session(request)

            if session.new:
                raise HTTPUnauthorized
            
            session.changed()
            
            return await handler(*args, **kwargs)
    
        return wrapper

    return _auth_guard

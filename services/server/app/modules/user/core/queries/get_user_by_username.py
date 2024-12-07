from aiohttp.web_exceptions import HTTPNotFound
from db import get_db_cursor
from psycopg import AsyncCursor
from psycopg.rows import class_row
from vsnder.models.user import User

SELECT_USER = """
SELECT * 
FROM "user"
WHERE "username" = %(username)s;
"""


async def get_user_by_username(username: str) -> User:
    async with get_db_cursor(get_user_by_username.__name__) as cursor:
        return await _get_user_by_username(cursor, username)


async def _get_user_by_username(cursor: AsyncCursor, username: str) -> User:
    cursor.row_factory = class_row(User)

    await cursor.execute(SELECT_USER, {"username": username})
    result = await cursor.fetchone()

    if not result:
        raise HTTPNotFound("Пользователь не найден")

    return result

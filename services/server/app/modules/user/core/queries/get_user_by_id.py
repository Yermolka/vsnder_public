from aiohttp.web_exceptions import HTTPNotFound
from db import get_db_cursor
from psycopg import AsyncCursor
from psycopg.rows import class_row
from vsnder.models.user import User

SELECT_USER = """
SELECT * 
FROM "user"
WHERE "id" = %(id)s;
"""


async def get_user_by_id(id: int) -> User:
    async with get_db_cursor(get_user_by_id.__name__) as cursor:
        return await _get_user_by_id(cursor, id)


async def _get_user_by_id(cursor: AsyncCursor, id: int) -> User:
    cursor.row_factory = class_row(User)
    
    await cursor.execute(SELECT_USER, {"id": id})
    result = await cursor.fetchone()

    if not result:
        raise HTTPNotFound("Пользователь не найден")
    
    return result

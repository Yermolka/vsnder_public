from werkzeug.exceptions import NotFound
from psycopg.rows import tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor
from models.user import User

SELECT_USER = """
SELECT "password_hash"
FROM "user"
WHERE "id" = %(id)s;
"""


async def get_user_password_by_id(id: int) -> User:
    async with get_db_cursor(get_user_password_by_id.__name__) as cursor:
        return await _get_user_password_by_id(cursor, id)


async def _get_user_password_by_id(cursor: AsyncCursor, id: int) -> User:
    cursor.row_factory = tuple_row
    
    await cursor.execute(SELECT_USER, {"id": id})
    result = await cursor.fetchone()

    if not result:
        raise NotFound(f"User {id} not found")
    
    return result[0]

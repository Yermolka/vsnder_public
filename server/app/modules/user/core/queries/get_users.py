from psycopg.rows import class_row
from psycopg import AsyncCursor
from db import get_db_cursor
from models.user import User

SELECT_USERS = """
SELECT * 
FROM "user"
ORDER BY %(order_by)s DESC;
"""


async def get_users(order_by: str = "modified") -> User:
    async with get_db_cursor(get_users.__name__) as cursor:
        return await _get_users(cursor, order_by)


async def _get_users(cursor: AsyncCursor, order_by: str) -> User:
    cursor.row_factory = class_row(User)
    
    await cursor.execute(SELECT_USERS, dict(order_by=order_by))
    result = await cursor.fetchall()

    return result

from psycopg.rows import class_row
from psycopg import Cursor
from db import get_db_cursor
from models.user import User

SELECT_USERS = """
SELECT * 
FROM "user"
ORDER BY %(order_by)s DESC;
"""


async def get_users(order_by: str = "modified") -> User:
    with get_db_cursor(get_users.__name__) as cursor:
        return await _get_users(cursor, order_by)


async def _get_users(cursor: Cursor, order_by: str) -> User:
    cursor.row_factory = class_row(User)
    
    cursor.execute(SELECT_USERS, dict(order_by=order_by))
    result = cursor.fetchall()

    return result

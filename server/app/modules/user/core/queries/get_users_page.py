from psycopg.rows import class_row
from psycopg import Cursor
from db import get_db_cursor
from models.user import User

SELECT_USERS = """
SELECT * 
FROM "user"
ORDER BY %(order_by)s ASC
LIMIT %(limit)s OFFSET %(offset)s;
"""


async def get_users_page(page: int, limit: int, order_by: str) -> list[User]:
    with get_db_cursor(get_users_page.__name__) as cursor:
        return await _get_users_page(cursor, page, limit, order_by)


async def _get_users_page(cursor: Cursor, page: int, limit: int, order_by: str) -> list[User]:
    cursor.row_factory = class_row(User)
    
    cursor.execute(SELECT_USERS, 
                   dict(
                       order_by=order_by,
                       limit=limit,
                       offset=limit * (page - 1)))
    result = cursor.fetchall()

    return result

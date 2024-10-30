from psycopg.rows import class_row
from psycopg import Cursor
from db import get_db_cursor
from models.user import User

SELECT_USERS = """
SELECT * 
FROM users;
"""


async def get_users() -> list[User]:
    with get_db_cursor(get_users.__name__) as cursor:
        return await _get_users(cursor)


async def _get_users(cursor: Cursor) -> list[User]:
    cursor.row_factory = class_row(User)

    cursor.execute(SELECT_USERS)

    return cursor.fetchall()

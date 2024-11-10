from werkzeug.exceptions import NotFound
from psycopg.rows import class_row
from psycopg import Cursor
from db import get_db_cursor
from models.user import User

SELECT_USER = """
SELECT * 
FROM "user"
WHERE "username" = %(username)s;
"""


async def get_user_by_username(username: str) -> User:
    with get_db_cursor(get_user_by_username.__name__) as cursor:
        return await _get_user_by_username(cursor, username)


async def _get_user_by_username(cursor: Cursor, username: str) -> User:
    cursor.row_factory = class_row(User)
    
    cursor.execute(SELECT_USER, {"username": username})
    result = cursor.fetchone()

    if not result:
        raise NotFound(f"User {username} not found")
    
    return result

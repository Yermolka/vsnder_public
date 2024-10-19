from werkzeug.exceptions import NotFound
from psycopg.rows import dict_row
from psycopg import Cursor
from db import get_db_cursor

SELECT_USER = """
SELECT * 
FROM users
WHERE username = %(username)s;
"""


async def get_user_by_username(username: str) -> dict:
    with get_db_cursor(get_user_by_username.__name__) as cursor:
        return await _get_user_by_username(cursor, username)


async def _get_user_by_username(cursor: Cursor, username: str) -> dict:
    cursor.row_factory = dict_row
    
    cursor.execute(SELECT_USER, {"username": username})
    result = cursor.fetchone()

    if not result:
        raise NotFound(f"User {username} not found")
    
    return result

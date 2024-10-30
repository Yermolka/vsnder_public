from psycopg.rows import dict_row
from psycopg import Cursor
from db import get_db_cursor

SELECT_USERS = """
SELECT * 
FROM users;
"""

async def get_users() -> list[dict]:
    with get_db_cursor(get_users.__name__) as cursor:
        return await _get_users(cursor)


async def _get_users(cursor: Cursor) -> list[dict]:
    cursor.row_factory = dict_row
    
    cursor.execute(SELECT_USERS)

    return cursor.fetchall()

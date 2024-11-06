from psycopg.rows import tuple_row
from psycopg import Cursor
from db import get_db_cursor
from server.app.modules.user.core.queries.get_user_by_username import _get_user_by_username

SELECT_WITH_PASSWORD = """
SELECT password = crypt(%(password)s, password)
FROM users
WHERE username = %(username)s;
"""


async def get_user_password_by_username(username: str, password: str) -> int:
    with get_db_cursor(get_user_password_by_username.__name__) as cursor:
        _user = await _get_user_by_username(cursor, username)

        return await _get_user_password_by_username(cursor, username, password)
            

async def _get_user_password_by_username(cursor: Cursor, username: str, password: str) -> int:
    cursor.row_factory = tuple_row

    cursor.execute(SELECT_WITH_PASSWORD, {"username": username, "password": password})
    result = cursor.fetchone()
    
    if not result:
        return None

    return result[0]

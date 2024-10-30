from psycopg.rows import tuple_row
from psycopg import Cursor
from werkzeug.exceptions import Forbidden
from db import get_db_cursor
from queries.get_user_by_username import _get_user_by_username

SELECT_WITH_PASSWORD = """
SELECT password = crypt(%(password)s, password)
FROM users
WHERE username = %(username)s;
"""

UPDATE_USER_PASSWORD = """
UPDATE users
SET password = crypt(%(password)s, gen_salt('bf'))
WHERE username = %(username)s
RETURNING users."id";
"""


async def change_password_by_username(username: str, old_password: str, new_password: str) -> int:
    with get_db_cursor(change_password_by_username.__name__) as cursor:
        _user = await _get_user_by_username(username)

        return await _change_password_by_username(cursor, username, old_password, new_password)
            

async def _change_password_by_username(cursor: Cursor, username: str, old_password: str, new_password: str) -> int:
    cursor.row_factory = tuple_row

    cursor.execute(SELECT_WITH_PASSWORD, {"username": username, "password": old_password})
    row = cursor.fetchone()
    
    if not row:
        raise Forbidden("Invalid password")

    cursor.execute(UPDATE_USER_PASSWORD, {"password": new_password, "username": username})
    result = cursor.fetchone()

    return result[0]

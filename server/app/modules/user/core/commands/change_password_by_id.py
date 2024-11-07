from psycopg import Cursor
from psycopg.rows import tuple_row

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id
from common.utils.auth import get_password_hash

UPDATE_USER = """
UPDATE users 
SET 
    password = %(password)s
WHERE id = %(id)s
RETURNING "id";
"""


async def change_password_by_id(id: int, password: str) -> int:
    with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, id)

        return await _change_password_by_id(cursor, id, password)


async def _change_password_by_id(cursor: Cursor, id: int, password: str) -> int:
    cursor.row_factory = tuple_row

    cursor.execute(UPDATE_USER, dict(id=id, password=get_password_hash(password)))
    result = cursor.fetchone()

    return result[0]

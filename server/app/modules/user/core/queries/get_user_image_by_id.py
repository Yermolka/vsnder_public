from psycopg.rows import tuple_row
from psycopg import Cursor
from db import get_db_cursor

SELECT_USER = """
SELECT "data", "media_type"
FROM "file"
WHERE "user_id" = %(user_id)s;
"""


async def get_user_image_by_id(user_id: int) -> bytes:
    with get_db_cursor(get_user_image_by_id.__name__) as cursor:
        return await _get_user_image_by_id(cursor, user_id)


async def _get_user_image_by_id(cursor: Cursor, user_id: int) -> bytes:
    cursor.row_factory = tuple_row

    cursor.execute(SELECT_USER, {"user_id": user_id})
    result = cursor.fetchone()

    if not result:
        return None

    return result[0], result[1]

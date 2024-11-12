from psycopg.rows import tuple_row
from psycopg import Cursor
from db import get_db_cursor

SELECT_IMAGE = """
SELECT "id"
FROM "file"
WHERE "user_id" = %(user_id)s;
"""


async def check_user_image_by_id(user_id: int) -> bool:
    with get_db_cursor(check_user_image_by_id.__name__) as cursor:
        return await _check_user_image_by_id(cursor, user_id)


async def _check_user_image_by_id(cursor: Cursor, user_id: int) -> bool:
    cursor.row_factory = tuple_row

    cursor.execute(SELECT_IMAGE, {"user_id": user_id})
    result = cursor.fetchone()

    return result is not None

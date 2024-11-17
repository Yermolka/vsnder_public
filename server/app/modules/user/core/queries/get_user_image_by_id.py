from typing import Tuple
from psycopg.rows import tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor

SELECT_IMAGE = """
SELECT "data", "media_type"
FROM "file"
WHERE "user_id" = %(user_id)s;
"""


async def get_user_image_by_id(user_id: int) -> Tuple[bytes, str]:
    async with get_db_cursor(get_user_image_by_id.__name__) as cursor:
        return await _get_user_image_by_id(cursor, user_id)


async def _get_user_image_by_id(cursor: AsyncCursor, user_id: int) -> Tuple[bytes, str]:
    cursor.row_factory = tuple_row

    await cursor.execute(SELECT_IMAGE, {"user_id": user_id})
    result = await cursor.fetchone()

    if not result:
        return None

    return result[0], result[1]

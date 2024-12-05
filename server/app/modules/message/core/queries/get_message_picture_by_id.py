from werkzeug.exceptions import NotFound
from psycopg.rows import tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor

SELECT_IMAGE = """
SELECT "picture", "media_type"
FROM "message"
WHERE "id" = %(id)s;
"""

async def get_message_picture_by_id(id: int) -> tuple[bytes, str]:
    async with get_db_cursor(get_message_picture_by_id.__name__) as cursor:
        return await _get_message_for_user_by_id(cursor, id)


async def _get_message_for_user_by_id(cursor: AsyncCursor, id: int) -> tuple[bytes, str]:
    cursor.row_factory = tuple_row

    await cursor.execute(SELECT_IMAGE, dict(id=id))
    result = await cursor.fetchone()

    if result is None:
        raise NotFound(f"message with id {id} not found")
    
    return result[0], result[1]

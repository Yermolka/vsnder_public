from psycopg.rows import tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor

SELECT_MESSAGES = """
SELECT "id", "text"
FROM "message"
WHERE "receiver_id" = %(receiver_id)s;
"""

COUNT_MESSAGES = """
SELECT COUNT(*)
FROM "message"
WHERE "receiver_id" = %(receiver_id)s;
"""


async def get_messages_for_user_by_id(id: int) -> list[tuple[int, str]]:
    async with get_db_cursor(get_messages_for_user_by_id.__name__) as cursor:
        return await _get_messages_for_user_by_id(cursor, id)


async def _get_messages_for_user_by_id(cursor: AsyncCursor, id: int) -> list[tuple[int, str]]:
    cursor.row_factory = tuple_row
    
    await cursor.execute(COUNT_MESSAGES, dict(receiver_id=id))
    count = await cursor.fetchone()

    if count == 0:
        return []

    await cursor.execute(SELECT_MESSAGES, dict(receiver_id=id))
    result = await cursor.fetchall()
    
    return result

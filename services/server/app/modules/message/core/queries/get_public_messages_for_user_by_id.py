from psycopg.rows import class_row, tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor
from vsnder.models.message import Message

SELECT_MESSAGES = """
SELECT *
FROM "message"
WHERE "receiver_id" = %(receiver_id)s
    AND "public" = TRUE;
"""

COUNT_MESSAGES = """
SELECT COUNT(*)
FROM "message"
WHERE "receiver_id" = %(receiver_id)s
    AND "public" = TRUE;
"""


async def get_public_messages_for_user_by_id(id: int) -> list[Message]:
    async with get_db_cursor(get_public_messages_for_user_by_id.__name__) as cursor:
        return await _get_public_messages_for_user_by_id(cursor, id)


async def _get_public_messages_for_user_by_id(cursor: AsyncCursor, id: int) -> list[Message]:
    cursor.row_factory = tuple_row
    
    await cursor.execute(COUNT_MESSAGES, dict(receiver_id=id))
    count = await cursor.fetchone()

    if count[0] == 0:
        return []

    cursor.row_factory = class_row(Message)

    await cursor.execute(SELECT_MESSAGES, dict(receiver_id=id))
    result = await cursor.fetchall()
    
    return result

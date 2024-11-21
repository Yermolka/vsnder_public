from psycopg.rows import tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor

SELECT_MESSAGES = """
SELECT "text"
FROM "message"
WHERE "receiver_id" = %(receiver_id)s;
"""


async def get_messages_for_user_by_id(id: int) -> list[str]:
    async with get_db_cursor(get_messages_for_user_by_id.__name__) as cursor:
        return await _get_messages_for_user_by_id(cursor, id)


async def _get_messages_for_user_by_id(cursor: AsyncCursor, id: int) -> list[str]:
    cursor.row_factory = tuple_row
    
    await cursor.execute(SELECT_MESSAGES, dict(receiver_id=id))
    result = await cursor.fetchall()
    
    return [r[0] for r in result]

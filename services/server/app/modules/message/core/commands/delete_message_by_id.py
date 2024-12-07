from psycopg import AsyncCursor
from psycopg.rows import tuple_row

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id

DELETE_MESSAGE = """
DELETE FROM "message" 
WHERE "id" = %(id)s AND "receiver_id" = %(user_id)s 
RETURNING "id";
"""


async def delete_message_by_id(user_id: int, id: int) -> None:
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, user_id)

        return await _delete_message_by_id(cursor, user_id, id)


async def _delete_message_by_id(cursor: AsyncCursor, user_id: int, id: int) -> None:
    cursor.row_factory = tuple_row

    await cursor.execute(DELETE_MESSAGE, dict(id=id, user_id=user_id))
    await cursor.fetchone()

    return

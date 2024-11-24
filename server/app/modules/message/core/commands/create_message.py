from psycopg import AsyncCursor
from psycopg.rows import tuple_row

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id

INSERT_MESSAGE = """
INSERT INTO "message" ("receiver_id", "text", "picture", "media_type")
VALUES (%(receiver_id)s, %(text)s, %(picture)s, %(media_type)s)
RETURNING "id";
"""


async def create_message(receiver_id: int, text: str | None, picture: bytes | None, media_type: str | None) -> int:
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, receiver_id)

        return await _create_message(cursor, receiver_id, text, picture, media_type)


async def _create_message(cursor: AsyncCursor, receiver_id: int, text: str | None, picture: bytes | None, media_type: str | None) -> int:
    cursor.row_factory = tuple_row

    await cursor.execute(INSERT_MESSAGE, dict(receiver_id=receiver_id, text=text, picture=picture, media_type=media_type))
    result = await cursor.fetchone()

    return result[0]

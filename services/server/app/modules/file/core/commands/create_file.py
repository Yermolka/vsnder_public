from psycopg import AsyncCursor
from psycopg.rows import tuple_row

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id

INSERT_FILE = """
INSERT INTO "file" ("user_id", "media_type", "data")
VALUES (%(user_id)s, %(media_type)s, %(data)s)
RETURNING "id";
"""


async def create_file(user_id: int, picture: bytes, media_type: str) -> int:
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, user_id)

        return await _create_file(cursor, user_id, picture, media_type)


async def _create_file(cursor: AsyncCursor, user_id: int, picture: bytes, media_type: str) -> int:
    cursor.row_factory = tuple_row

    await cursor.execute(INSERT_FILE, dict(user_id=user_id, media_type=media_type, data=picture))
    result = await cursor.fetchone()

    return result[0]

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id
from psycopg import AsyncCursor
from psycopg.rows import tuple_row

UPDATE_USER_IMAGE = """
UPDATE "user" SET 
    "file_id" = %(file_id)s
WHERE "id" = %(user_id)s
RETURNING "id";
"""


async def set_user_image_by_user_id(user_id: int, file_id: int):
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, user_id)

        return await _set_user_image_by_user_id(cursor, user_id, file_id)
    

async def _set_user_image_by_user_id(cursor: AsyncCursor, user_id: int, file_id: int):
    cursor.row_factory = tuple_row

    await cursor.execute(UPDATE_USER_IMAGE, dict(user_id=user_id, file_id=file_id))
    res = await cursor.fetchone()

    return res[0]

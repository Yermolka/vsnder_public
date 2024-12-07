from common.utils.auth import get_password_hash
from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id
from psycopg import AsyncCursor
from psycopg.rows import tuple_row

UPDATE_USER = """
UPDATE "user"
SET 
    "password_hash" = %(password_hash)s
WHERE "id" = %(id)s
RETURNING "id";
"""


async def change_password_by_id(id: int, password: str) -> int:
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, id)

        return await _change_password_by_id(cursor, id, password)


async def _change_password_by_id(cursor: AsyncCursor, id: int, password: str) -> int:
    cursor.row_factory = tuple_row

    await cursor.execute(UPDATE_USER, dict(id=id, password_hash=get_password_hash(password)))
    result = await cursor.fetchone()

    return result[0]

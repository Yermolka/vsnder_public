from psycopg import AsyncCursor
from psycopg.rows import tuple_row

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id

INSERT_LOG = """
INSERT INTO "analytic_logs" ("user_id", "data")
VALUES (%(user_id)s, %(data)s)
RETURNING "id";
"""

SELECT_LAST_ROW = """
SELECT "user_id", "data" FROM "analytic_logs"
ORDER BY "id" DESC LIMIT 1;
"""


async def create_log_entry(user_id: int, data: str) -> int:
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, user_id)

        return await _create_log_entry(cursor, user_id, data)
    

async def _create_log_entry(cursor: AsyncCursor, user_id: int, data: str) -> int:
    cursor.row_factory = tuple_row

    await cursor.execute(SELECT_LAST_ROW)
    result = await cursor.fetchone()

    if result and result[0] == user_id and result[1] == data:
        return 0

    await cursor.execute(INSERT_LOG, {"user_id": user_id, "data": data})

    result = await cursor.fetchone()

    return result[0]


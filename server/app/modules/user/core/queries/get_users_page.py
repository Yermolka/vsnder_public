from typing import Tuple
from psycopg.rows import class_row, tuple_row
from psycopg import AsyncCursor, sql
from db import get_db_cursor
from models.user import User

SELECT_USERS = """
SELECT * 
FROM "user"
ORDER BY %(order_by)s ASC
LIMIT %(limit)s OFFSET %(offset)s;
"""

COUNT_USERS = """
SELECT COUNT(*)
FROM "user";
"""


async def get_users_page(
    page: int, limit: int, order_by: str
) -> Tuple[int, list[User]]:
    async with get_db_cursor(get_users_page.__name__) as cursor:
        return await _get_users_page(cursor, page, limit, order_by)


async def _get_users_page(
    cursor: AsyncCursor, page: int, limit: int, order_by: str
) -> Tuple[int, list[User]]:
    if order_by not in [
        "id",
        "first_name",
        "last_name",
        "age",
        "orientation",
        "year_of_study",
    ]:
        order_by = "id"

    cursor.row_factory = tuple_row
    await cursor.execute(COUNT_USERS)
    count = (await cursor.fetchone())[0]

    if count == 0:
        return 0, []

    cursor.row_factory = class_row(User)
    query = sql.SQL(
        """
                    SELECT * 
                    FROM "user"
                    ORDER BY {} ASC
                    """
        + f"LIMIT {limit} OFFSET {limit * (page - 1)};"
    )
    await cursor.execute(query.format(sql.Identifier(order_by)))
    result = await cursor.fetchall()

    return count, result

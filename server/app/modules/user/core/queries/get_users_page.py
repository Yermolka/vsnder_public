from typing import Tuple
from psycopg.rows import class_row, tuple_row
from psycopg import AsyncCursor, sql
from db import get_db_cursor
from models.user import User

SELECT_USERS = """
SELECT * 
FROM "user"
WHERE (
    "orientation" LIKE %(orientation)s
    OR %(orientation)s IS NULL
) AND (
    "year_of_study" = %(year_of_study)s
    OR %(year_of_study)s IS NULL
) AND (
    "status" LIKE %(status)s
    OR %(status)s IS NULL
)
ORDER BY %(order_by)s ASC
LIMIT %(limit)s OFFSET %(offset)s;
"""

COUNT_USERS = """
SELECT COUNT(*)
FROM "user"
WHERE (
    "orientation" LIKE %(orientation)s
    OR %(orientation)s IS NULL
) AND (
    "year_of_study" = %(year_of_study)s
    OR %(year_of_study)s IS NULL
) AND (
    "status" LIKE %(status)s
    OR %(status)s IS NULL
);
"""


async def get_users_page(
    page: int,
    limit: int,
    order_by: str,
    orientation: str | None,
    year_of_study: int | None,
    status: str | None,
) -> Tuple[int, list[User]]:
    async with get_db_cursor(get_users_page.__name__) as cursor:
        return await _get_users_page(
            cursor, page, limit, order_by, orientation, year_of_study, status
        )


async def _get_users_page(
    cursor: AsyncCursor,
    page: int,
    limit: int,
    order_by: str,
    orientation: str | None,
    year_of_study: int | None,
    status: str | None,
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

    if orientation is not None and orientation not in [
        "Психология",
        "Социология",
        "Политология",
        "ГМУ",
    ]:
        orientation = None

    if year_of_study is not None and year_of_study not in [1, 2, 3, 4]:
        year_of_study = None

    if status is not None and status not in [
        "Замужем/Женат",
        "В отношениях",
        "Схожу на свидание",
        "Чиллю соло",
    ]:
        status = None

    cursor.row_factory = tuple_row
    await cursor.execute(
        COUNT_USERS,
        dict(orientation=orientation, year_of_study=year_of_study, status=status),
    )
    count = (await cursor.fetchone())[0]

    if count == 0:
        return 0, []

    # limit = max(1, min(limit, count))
    # page = max(1, min(page, count // limit + 1))

    cursor.row_factory = class_row(User)
    query = sql.SQL(
        """
                    SELECT * 
                    FROM "user"
                    WHERE (
                        "orientation" LIKE {orientation}
                        OR {orientation} IS NULL
                    ) AND (
                        "year_of_study" = {year_of_study}
                        OR {year_of_study} IS NULL
                    ) AND (
                        "status" LIKE {status}
                        OR {status} IS NULL
                    )
                    """
        + """ORDER BY {order_by} ASC """
        + "LIMIT {limit} OFFSET {offset};"
    )
    await cursor.execute(
        query.format(
            order_by=sql.Identifier(order_by),
            orientation=orientation,
            year_of_study=year_of_study,
            status=status,
            limit=limit,
            offset=limit * (page - 1),
        )
    )
    result = await cursor.fetchall()

    return count, result

from aiohttp.web_exceptions import HTTPNotFound
from psycopg.rows import tuple_row
from psycopg import AsyncCursor
from db import get_db_cursor

SELECT_FILE_DATA = """
SELECT "data", "media_type"
FROM "file"
WHERE "id" = %(id)s;
"""


async def get_file_by_id(file_id: int) -> tuple[bytes, str]:
    async with get_db_cursor(get_file_by_id.__name__) as cursor:
        return await _get_file_by_id(cursor, file_id)
    

async def _get_file_by_id(cursor: AsyncCursor, file_id: int) -> tuple[bytes, str]:
    cursor.row_factory = tuple_row

    await cursor.execute(SELECT_FILE_DATA, {"id": file_id})
    result = await cursor.fetchone()

    if not result:
        raise HTTPNotFound("Файл не найден")
    
    return result[0], result[1]

from psycopg import AsyncCursor
from psycopg.rows import tuple_row

from db import get_db_cursor
from modules.user.core.queries.get_user_by_id import _get_user_by_id

UPDATE_USER_IMAGE = """
UPDATE "file" SET 
    "data" = %(image)s,
    "media_type" = %(media_type)s
WHERE "user_id" = %(user_id)s
RETURNING "id";
"""

INSERT_USER_IMAGE = """
INSERT INTO "file" ("user_id", "data", "media_type") 
VALUES (%(user_id)s, %(image)s, %(media_type)s)
RETURNING "id";
"""

GET_USER_IMAGE_ID = """
SELECT "id"
FROM "file"
WHERE "user_id" = %(user_id)s;
"""

UPDATE_USER_HAS_AVATAR = """
UPDATE "user" SET
    "has_avatar" = TRUE
WHERE "id" = %(user_id)s
RETURNING "id";
"""


async def set_user_image_by_user_id(user_id: int, image: bytes, media_type: str):
    async with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, user_id)

        return await _set_user_image_by_user_id(cursor, user_id, image, media_type)
    

async def _set_user_image_by_user_id(cursor: AsyncCursor, user_id: int, image: bytes, media_type: str):
    cursor.row_factory = tuple_row

    await cursor.execute(GET_USER_IMAGE_ID, dict(user_id=user_id))
    result = await cursor.fetchone()
    
    if not result:
        await cursor.execute(INSERT_USER_IMAGE, dict(user_id=user_id, image=image, media_type=media_type))
        result = await cursor.fetchone()
    else:
        await cursor.execute(UPDATE_USER_IMAGE, dict(user_id=user_id, image=image, media_type=media_type))
        result = await cursor.fetchone()

    file_id = result[0]

    if result:
        await cursor.execute(UPDATE_USER_HAS_AVATAR, dict(user_id=user_id))

    return file_id

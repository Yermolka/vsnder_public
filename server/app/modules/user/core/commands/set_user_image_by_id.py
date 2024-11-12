from psycopg import Cursor
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

async def set_user_image_by_user_id(user_id: int, image: bytes, media_type: str):
    with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, user_id)

        return await _set_user_image_by_user_id(cursor, user_id, image, media_type)
    

async def _set_user_image_by_user_id(cursor: Cursor, user_id: int, image: bytes, media_type: str):
    cursor.row_factory = tuple_row

    cursor.execute(GET_USER_IMAGE_ID, dict(user_id=user_id))
    result = cursor.fetchone()
    
    if not result:
        cursor.execute(INSERT_USER_IMAGE, dict(user_id=user_id, image=image, media_type=media_type))
        result = cursor.fetchone()
    else:
        cursor.execute(UPDATE_USER_IMAGE, dict(user_id=user_id, image=image, media_type=media_type))
        result = cursor.fetchone()

    return result[0]

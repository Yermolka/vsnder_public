from werkzeug.exceptions import NotFound
from psycopg.rows import class_row
from psycopg import Cursor
from db import get_db_cursor
from models.user import User

SELECT_USER = """
SELECT * 
FROM users
WHERE id = %(id)s;
"""


async def get_user_by_id(id: int) -> User:
    with get_db_cursor(get_user_by_id.__name__) as cursor:
        return await _get_user_by_id(cursor, id)


async def _get_user_by_id(cursor: Cursor, id: int) -> User:
    cursor.row_factory = class_row(User)
    
    cursor.execute(SELECT_USER, {"id": id})
    result = cursor.fetchone()

    if not result:
        raise NotFound(f"User {id} not found")
    
    return result

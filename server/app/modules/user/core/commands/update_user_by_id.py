from psycopg import Cursor
from psycopg.rows import tuple_row
from datetime import datetime

from db import get_db_cursor
from dto.user import PostUserDto
from modules.user.core.queries.get_user_by_id import _get_user_by_id

UPDATE_USER = """
UPDATE "user"
SET 
    "age" = %(age)s,
    "orientation" = %(orientation)s,
    "interests" = %(interests)s,
    "vsn_interests" = %(vsn_interests)s,
    "places_to_visit" = %(places_to_visit)s,
    "study_places" = %(study_places)s,
    "music" = %(music)s,
    "favorite_movies" = %(favorite_movies)s,
    "religion" = %(religion)s,
    "status" = %(status)s,
    "future_plans" = %(future_plans)s,
    "family_opinion" = %(family_opinion)s,
    "favorite_programming_language" = %(favorite_programming_language)s,
    "lizards_or_russians" = %(lizards_or_russians)s,
    "smoking" = %(smoking)s,
    "top_3_people" = %(top_3_people)s,
    "drinking" = %(drinking)s,
    "modified" = %(modified)s
WHERE id = %(id)s
RETURNING "id";
"""


async def update_user_by_id(id: int, dto: PostUserDto) -> int:
    with get_db_cursor() as cursor:
        _user = await _get_user_by_id(cursor, id)

        return await _update_user_by_id(cursor, id, dto)


async def _update_user_by_id(cursor: Cursor, id: int, dto: PostUserDto) -> int:
    cursor.row_factory = tuple_row

    cursor.execute(UPDATE_USER, dict(id=id, modified=datetime.now(), **dto.to_dict()))
    result = cursor.fetchone()

    return result[0]

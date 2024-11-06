from psycopg.rows import tuple_row
from psycopg import Cursor
from db import get_db_cursor
from server.app.modules.user.core.queries.get_user_by_username import _get_user_by_username
from models.user import PutUserDto

UPDATE_USER = """
UPDATE users
SET
    age = %(age)s,
    orientation = %(orientation)s,
    interests = %(interests)s,
    vsn_interests = %(vsn_interests)s,
    places_to_visit = %(places_to_visit)s,
    study_places = %(study_places)s,
    music = %(music)s,
    favorite_movies = %(favorite_movies)s,
    religion = %(religion)s,
    status = %(status)s,
    future_plans = %(future_plans)s,
    family_opinion = %(family_opinion)s,
    favorite_programming_language = %(favorite_programming_language)s,
    lizards_or_russians = %(lizards_or_russians)s,
    smoking = %(smoking)s,
    top_3_people = %(top_3_people)s,
    drinking = %(drinking)s
WHERE username = %(username)s
RETURNING "id";
"""


async def update_user_by_username(dto: PutUserDto) -> int:
    with get_db_cursor() as cursor:
        _user = await _get_user_by_username(cursor, dto.username)

        return await _update_user_by_username(cursor, dto)
        

async def _update_user_by_username(cursor: Cursor, dto: PutUserDto) -> int:
    cursor.row_factory = tuple_row

    cursor.execute(UPDATE_USER, dto.to_dict())
    result = cursor.fetchone()
    
    return result[0]

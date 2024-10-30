from psycopg.rows import tuple_row
from psycopg import Cursor
from db import get_db_cursor
from queries.get_user_by_username import _get_user_by_username

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

#TODO: change data to put user dto!!
async def update_user_by_username(username: str, data: dict) -> int:
    with get_db_cursor() as cursor:
        _user = await _get_user_by_username(cursor, username)

        return await _update_user_by_username(cursor, username, data)
        

# pass user model, get username from it
async def _update_user_by_username(cursor: Cursor, username: str, data: dict) -> int:
    cursor.row_factory = tuple_row
    data["username"] = username

    cursor.execute(UPDATE_USER, data)
    result = cursor.fetchone()
    
    return result[0]

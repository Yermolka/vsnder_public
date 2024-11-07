from aiohttp.web import Request, json_response
from aiohttp_session import get_session
from dto.user import GetUserDto

from common.utils.auth import auth_guard
from common.consts import USER_SESSION_USER_ID_KEY
from modules.user.core.queries.get_users import get_users
from random import choice


@auth_guard()
async def get_user_handler(request: Request):
    session = await get_session(request)
    user_id = session[USER_SESSION_USER_ID_KEY]

    users = await get_users()

    user = choice(list(filter(lambda u: u.id != user_id, users)))

    return json_response(GetUserDto.from_model(user).to_dict())

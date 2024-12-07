from random import choice

from aiohttp.web import Request, json_response
from aiohttp_session import get_session
from common.consts import USER_SESSION_USER_ID_KEY
from common.utils.auth import auth_guard
from modules.user.core.commands.create_log_entry import create_log_entry
from modules.user.core.queries.get_users import get_users
from vsnder.dto.user import GetUserDto


@auth_guard()
async def get_random_user_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get a random user
    tags:
        - user
    responses:
        "200":
            description: User data
            content:
                application/json:
                    schema:
                        $ref: "#/components/schemas/GetUserDto"
        "401":
            description: Unauthorized
            content:
                text/plain:
                    schema:
                        type: string
        "500":
            description: Internal server error
            content:
                text/plain:
                    schema:
                        type: string
    """

    session = await get_session(request)
    user_id = session[USER_SESSION_USER_ID_KEY]

    users = await get_users()

    user = choice(list(filter(lambda u: u.id != user_id, users)))

    await create_log_entry(user_id, "get_random_user")

    return json_response(GetUserDto.from_model(user).to_dict())

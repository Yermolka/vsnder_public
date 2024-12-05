from aiohttp.web import Request, json_response
from aiohttp_session import get_session
from dto.user import GetUserDto

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from common.consts import USER_SESSION_USER_ID_KEY
from modules.user.core.queries.get_user_by_id import get_user_by_id
from modules.user.core.commands.create_log_entry import create_log_entry


@auth_guard()
async def get_user_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get user's avatar
    tags:
        - user
    parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
    responses:
        "200":
            description: User data
            content:
                application/json:
                    schema:
                        $ref: "$/components/schemas/GetUserDto"
        "400":
            description: List of reasons<br/><br/>
                - path param user_id is too long<br/>
                - specify path param user_id<br/>
            content:
                text/plain:
                    schema:
                        type: string
        "401":
            description: Unauthorized
            content:
                text/plain:
                    schema:
                        type: string
        "404":
            description: User not found
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
    session_user_id = session[USER_SESSION_USER_ID_KEY]

    user_id = get_int_path_param(request, "user_id")

    user = await get_user_by_id(user_id)

    await create_log_entry(session_user_id, f"get_user: {user_id}")

    return json_response(GetUserDto.from_model(user).to_dict())

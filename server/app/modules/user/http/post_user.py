from aiohttp.web import Request, json_response
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_session import get_session
from dto.user import PostUserDto

from common.utils.auth import auth_guard
from common.consts import USER_SESSION_USER_ID_KEY
from modules.user.core.commands.update_user_by_id import update_user_by_id
from modules.user.core.commands.create_log_entry import create_log_entry


@auth_guard()
async def post_user_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Update profile
    tags:
        - user
    responses:
        "200":
            description: Profile updated
            content:
                application/json:
                    schema:
                        type: integer
        "400":
            description: Bad request
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

    try:
        dto = PostUserDto.from_dict(await request.json())
        dto.to_dict()
    except Exception:
        raise HTTPBadRequest()
    
    await update_user_by_id(session_user_id, dto)

    await create_log_entry(session_user_id, "profile_update")

    return json_response(session_user_id)

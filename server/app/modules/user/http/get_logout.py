from aiohttp.web import Request, Response
from aiohttp_session import get_session
from common.consts import USER_SESSION_USER_ID_KEY
from common.utils.auth import auth_guard
from modules.user.core.commands.create_log_entry import create_log_entry


@auth_guard()
async def user_logout_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get has_image for user
    tags:
        - user
        - auth
    responses:
        "200":
            description: Logged out
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
        "500":
            description: Internal server error
            content:
                text/plain:
                    schema:
                        type: string
    """

    session = await get_session(request)
    user_id = session[USER_SESSION_USER_ID_KEY]

    session.clear()
    session.invalidate()

    await create_log_entry(user_id, "logout")

    return Response(text="logged out")

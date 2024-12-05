from aiohttp.web import Request, json_response
from aiohttp_session import new_session
from aiohttp.web_exceptions import HTTPUnauthorized

from common.consts import USER_SESSION_USER_ID_KEY
from dto.auth import PostAuthDto
from modules.user.core.utils.auth_by_password import auth_by_password
from modules.user.core.commands.create_log_entry import create_log_entry


async def user_login_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Login
    tags:
        - user
        - auth
    responses:
        "200":
            description: ok
            content:
                application/json:
                    schema:
                        type: object
                        required:
                            - userId
                        properties:
                            userId:
                                type: integer
        "401":
            description: Unauthorized
            content:
                text/plain:
                    schema:
                        type: string
        "404":
            description: Not found
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

    try:
        body = await request.json()
        dto = PostAuthDto.from_dict(body)

        user = await auth_by_password(dto.username, dto.password)

        if not user:
            raise HTTPUnauthorized(text="Неверный логин или пароль")
        
        session = await new_session(request)
        session[USER_SESSION_USER_ID_KEY] = user.id
        session.changed()
    except Exception as e:
        raise HTTPUnauthorized(text=str(e))
    
    await create_log_entry(user.id, "login")

    return json_response({"userId": user.id})

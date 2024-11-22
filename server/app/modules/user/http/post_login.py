from aiohttp.web import Request, json_response
from aiohttp_session import new_session
from aiohttp.web_exceptions import HTTPUnauthorized

from common.consts import USER_SESSION_USER_ID_KEY
from dto.auth import PostAuthDto
from modules.user.core.utils.auth_by_password import auth_by_password
from modules.user.core.commands.create_log_entry import create_log_entry


async def user_login_handler(request: Request):
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

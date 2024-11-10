from aiohttp.web import Request, json_response
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_session import get_session
from dto.user import PostUserDto

from common.utils.auth import auth_guard
from common.consts import USER_SESSION_USER_ID_KEY
from modules.user.core.commands.update_user_by_id import update_user_by_id


@auth_guard()
async def post_user_handler(request: Request):
    session = await get_session(request)
    session_user_id = session[USER_SESSION_USER_ID_KEY]

    try:
        dto = PostUserDto.from_dict(await request.json())
    except Exception as e:
        raise HTTPBadRequest(text=str(e))
    
    await update_user_by_id(session_user_id, dto)

    return json_response(data={"user_id": session_user_id})

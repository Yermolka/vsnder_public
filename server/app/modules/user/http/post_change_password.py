from aiohttp.web import Request, json_response
from aiohttp_session import get_session
from aiohttp.web_exceptions import HTTPBadRequest

from common.utils.auth import auth_guard, check_password_match
from common.consts import USER_SESSION_USER_ID_KEY
from modules.user.core.commands.change_password_by_id import change_password_by_id
from modules.user.core.queries.get_user_password_by_id import get_user_password_by_id
from modules.user.core.commands.create_log_entry import create_log_entry


@auth_guard()
async def post_change_password_handler(request: Request):
    session = await get_session(request)
    user_id = session[USER_SESSION_USER_ID_KEY]

    user_password = await get_user_password_by_id(user_id)
    data = await request.json()

    old_password = data["old_password"]
    new_password = data["new_password"]

    if not check_password_match(old_password, user_password):
        raise HTTPBadRequest(text="Password is not correct")
    
    if len(new_password) < 6:
        raise HTTPBadRequest(text="Password should be at least 6 characters long")
    
    await change_password_by_id(user_id, new_password)

    await create_log_entry(user_id, "change_password")

    return json_response(data={"user_id": user_id})

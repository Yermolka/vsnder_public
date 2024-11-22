from aiohttp.web import Request, json_response
from aiohttp_session import get_session
from aiohttp.web_exceptions import HTTPForbidden

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from common.consts import USER_SESSION_USER_ID_KEY
from modules.message.core.queries.get_messages_for_user_by_id import get_messages_for_user_by_id

@auth_guard()
async def get_messages_handler(request: Request):
    receiver_id = get_int_path_param(request, "receiver_id")
    session = await get_session(request)

    if int(session[USER_SESSION_USER_ID_KEY]) != receiver_id:
        raise HTTPForbidden()

    messages = await get_messages_for_user_by_id(receiver_id)

    return json_response([{"id": message[0], "text": message[1]} for message in messages])

from aiohttp.web import Request, Response
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_session import get_session

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from common.consts import USER_SESSION_USER_ID_KEY
from modules.message.core.commands.create_message import create_message

@auth_guard()
async def post_message_handler(request: Request):
    receiver_id = get_int_path_param(request, "receiver_id")
    session = await get_session(request)

    if int(session[USER_SESSION_USER_ID_KEY]) == receiver_id:
        return Response()

    try:
        text = (await request.json())["text"]
    except KeyError:
        return HTTPBadRequest()

    await create_message(receiver_id, text)

    return Response()

from aiohttp.web import Request, Response
from aiohttp_session import get_session
from common.utils.auth import auth_guard

@auth_guard()
async def user_logout_handler(request: Request):
    session = await get_session(request)
    session.clear()
    session.invalidate()

    return Response(text="logged out")

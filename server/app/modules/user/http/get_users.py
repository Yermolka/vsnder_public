from aiohttp.web import Request, json_response
from dto.user import GetUserDto

from common.utils.auth import auth_guard
from modules.user.core.queries.get_users import get_users


@auth_guard()
async def get_users_handler(request: Request):
    users = await get_users()

    return json_response(
        {"users": list(map(lambda u: GetUserDto.from_model(u).to_dict(), users))}
    )

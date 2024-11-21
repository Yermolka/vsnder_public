from aiohttp.web import Request, json_response
from dto.user import GetShortUserDto

from common.utils.auth import auth_guard
from modules.user.core.queries.get_users import get_users


@auth_guard()
async def get_users_handler(_request: Request):
    users = await get_users()

    return json_response(
        list(map(lambda u: GetShortUserDto.from_model(u).to_dict(), users))
    )

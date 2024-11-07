from aiohttp.web import Request, json_response
from dto.user import GetUserDto

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from modules.user.core.queries.get_user_by_id import get_user_by_id


@auth_guard()
async def get_user_handler(request: Request):
    user_id = get_int_path_param(request, "user_id")

    user = await get_user_by_id(user_id)

    return json_response(GetUserDto.from_model(user).to_dict())

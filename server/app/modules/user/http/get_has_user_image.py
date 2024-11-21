from aiohttp.web import Request, Response

from common.utils.auth import auth_guard
from modules.user.core.queries.check_user_image_by_id import check_user_image_by_id
from common.utils.http import get_int_path_param


@auth_guard()
async def get_has_user_image_handler(request: Request):
    user_id = get_int_path_param(request, 'user_id')

    has_image = await check_user_image_by_id(user_id)

    if has_image:
        return Response(status=200)
    
    return Response(status=404)

from aiohttp.web import Request, json_response
from dto.user import GetShortUserDto

from common.utils.auth import auth_guard
from modules.user.core.queries.get_users_page import get_users_page
from common.utils.http import get_int_query_param, get_str_query_param


@auth_guard()
async def get_users_page_handler(request: Request):
    page = get_int_query_param(request, "page", 1)
    limit = get_int_query_param(request, "limit", 32)
    order_by = get_str_query_param(request, "orderBy", "id")

    if page < 1:
        page = 1

    if order_by not in [
        "id",
        "first_name",
        "last_name",
        "age",
        "orientation",
        "year_of_study",
    ]:
        order_by = "id"

    total, users = await get_users_page(page, limit, order_by)

    print(f"{page=} {order_by=}")

    return json_response(
        {
            "total": total,
            "users": list(
                map(lambda u: GetShortUserDto.from_model(u).to_dict(), users)
            ),
        }
    )

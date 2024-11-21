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
    orientation = get_str_query_param(request, "orientation", None, False)
    year_of_study = get_int_query_param(request, "year_of_study", None, False)
    status = get_str_query_param(request, "status", None, False)

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

    if orientation is not None and orientation not in ["Психология", "Социология", "Политология", "ГМУ"]:
        orientation = None

    if year_of_study is not None and year_of_study not in [1, 2, 3, 4]:
        year_of_study = None

    if status is not None and status not in ["Замужем/Женат", "В отношениях", "Схожу на свидание", "Чиллю соло"]:
        status = None

    total, users = await get_users_page(page, limit, order_by, orientation, year_of_study, status)

    return json_response(
        {
            "total": total,
            "users": list(
                map(lambda u: GetShortUserDto.from_model(u).to_dict(), users)
            ),
        }
    )

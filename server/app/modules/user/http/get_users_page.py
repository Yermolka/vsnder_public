from aiohttp.web import Request, json_response
from dto.user import GetShortUserDto

from common.utils.auth import auth_guard
from modules.user.core.queries.get_users_page import get_users_page
from common.utils.http import get_int_query_param, get_str_query_param


@auth_guard()
async def get_users_page_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get users
    tags:
        - user
    parameters:
        - in: query
          name: page
          required: false
          schema:
            type: integer
        - in: query
          name: limit
          required: false
          schema:
            type: integer
        - in: query
          name: orderBy
          required: false
          schema:
            type: string
            oneOf:
                - "id"
                - "first_name"
                - "last_name"
                - "age"
                - "orientation"
                - "year_of_study"
                - "modified"
        - in: query
          name: orientation
          required: false
          schema:
            type: string
            oneOf:
                - "Психология"
                - "Социология"
                - "Политология"
                - "ГМУ"
        - in: query
          name: year_of_study
          required: false
          schema:
            type: integer
        - in: query
          name: status
          required: false
          schema:
            type: string
            oneOf:
                - "Замужем/Женат"
                - "В отношениях"
                - "Схожу на свидание"
                - "Чиллю соло"
        - in: query
          name: query
          required: false
          schema:
            type: string
    responses:
        "200":
            description: Users array
            content:
                application/json:
                    schema:
                        type: object
                        required: 
                            - total
                            - users
                        properties:
                            total:
                                type: integer
                            users:
                                type: array
                                items:
                                    $ref: "#/components/schemas/GetShortUserDto"
        "400":
            description: List of reasons<br/><br/>
                - any query param is too long<br/>
                - any query param is invalid<br/>
            content:
                text/plain:
                    schema:
                        type: string
        "401":
            description: Unauthorized
            content:
                text/plain:
                    schema:
                        type: string
        "500":
            description: Internal server error
            content:
                text/plain:
                    schema:
                        type: string
    """

    page = get_int_query_param(request, "page", 1)
    limit = get_int_query_param(request, "limit", 32)
    order_by = get_str_query_param(request, "orderBy", "id")
    orientation = get_str_query_param(request, "orientation", None, False)
    year_of_study = get_int_query_param(request, "year_of_study", None, False)
    status = get_str_query_param(request, "status", None, False)
    query = get_str_query_param(request, "query", None, False)

    if page < 1:
        page = 1

    if order_by not in [
        "id",
        "first_name",
        "last_name",
        "age",
        "orientation",
        "year_of_study",
    ] or order_by == "id":
        order_by = "modified"

    if orientation is not None and orientation not in ["Психология", "Социология", "Политология", "ГМУ"]:
        orientation = None

    if year_of_study is not None and year_of_study not in [1, 2, 3, 4]:
        year_of_study = None

    if status is not None and status not in ["Замужем/Женат", "В отношениях", "Схожу на свидание", "Чиллю соло"]:
        status = None

    total, users = await get_users_page(page, limit, order_by, orientation, year_of_study, status, query)

    return json_response(
        {
            "total": total,
            "users": list(
                map(lambda u: GetShortUserDto.from_model(u).to_dict(), users)
            ),
        }
    )

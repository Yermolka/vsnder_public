from aiohttp.web import Request, Response

from common.utils.auth import auth_guard
from modules.user.core.queries.check_user_image_by_id import check_user_image_by_id
from common.utils.http import get_int_path_param


@auth_guard()
async def get_has_user_image_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get has_image for user
    tags:
        - user
        - file
    parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
    responses:
        "200":
            description: User has an avatar
        "400":
            description: List of reasons<br/><br/>
                - path param user_id is too long<br/>
                - specify path param user_id<br/>
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
        "404":
            description: User doesn't have an avatar
        "500":
            description: Internal server error
            content:
                text/plain:
                    schema:
                        type: string
    """

    user_id = get_int_path_param(request, "user_id")

    has_image = await check_user_image_by_id(user_id)

    if has_image:
        return Response(status=200)
    
    return Response(status=404)

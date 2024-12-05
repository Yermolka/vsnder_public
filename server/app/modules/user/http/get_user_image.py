from aiohttp.web import Request, StreamResponse
from aiohttp.web_exceptions import HTTPNotFound

from common.utils.auth import auth_guard
from modules.user.core.queries.get_user_image_by_id import get_user_image_by_id
from common.utils.http import get_int_path_param


@auth_guard()
async def get_user_image_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get user's avatar
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
            description: Image
            content:
                application/json:
                    schema:
                        type: bytes
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
            description: Image not found
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

    # Maybe store images in redis cache, invalidate on post image
    user_id = get_int_path_param(request, "user_id")

    img = await get_user_image_by_id(user_id)

    if not img:
        raise HTTPNotFound()

    data, media_type = img

    resp = StreamResponse()
    resp.content_type = _media_to_content_type(media_type)
    resp.content_length = len(data)

    await resp.prepare(request)
    await resp.write(data)
    await resp.write_eof()

    return resp


def _media_to_content_type(media_type: str):
    if media_type == "jpg":
        return "image/jpeg"

    if media_type == "png":
        return "image/png"

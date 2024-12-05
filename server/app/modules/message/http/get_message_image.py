from aiohttp.web import Request, StreamResponse
from aiohttp_session import get_session
from aiohttp.web_exceptions import HTTPForbidden

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from common.consts import USER_SESSION_USER_ID_KEY
from modules.message.core.queries.get_message_picture_by_id import (
    get_message_picture_by_id,
)


@auth_guard()
async def get_message_image_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get image for message
    tags:
        - message
        - file
    parameters:
        - in: path
          name: receiver_id
          required: true
          schema:
            type: integer
        - in: path
          name: id
          required: true
          schema:
            type: integer
    responses:
        "200":
            description: Image file
            content:
                image:
                    schema:
                        type: bytes
        "400":
            description: List of reasons<br/><br/>
                - path param id is too long<br/>
                - specify path param id<br/>
                - path param receiver_id is too long<br/>
                - specify path param receiver_id<br/>
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
            description: File not found
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

    receiver_id = get_int_path_param(request, "receiver_id")
    session = await get_session(request)

    if int(session[USER_SESSION_USER_ID_KEY]) != receiver_id:
        raise HTTPForbidden()

    message_id = get_int_path_param(request, "id")
    file = await get_message_picture_by_id(message_id)

    data, media_type = file

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

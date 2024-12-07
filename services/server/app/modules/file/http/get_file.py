from aiohttp.web import Request, StreamResponse

from common.utils.auth import auth_guard
from modules.file.core.queries.get_file_by_id import get_file_by_id
from common.utils.http import get_int_path_param


@auth_guard()
async def get_file_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get file by id
    tags:
        - file
    parameters:
        - in: path
          name: file_id
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
                - path param file_id is too long<br/>
                - specify path param file_id<br/>
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
    file_id = get_int_path_param(request, "file_id")

    data, media_type = await get_file_by_id(file_id)

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

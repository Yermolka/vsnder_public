from aiohttp.web import Request, json_response
from aiohttp.web_exceptions import HTTPBadRequest

from io import BytesIO
from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from modules.message.core.commands.create_message_response import create_message_response
from PIL import ImageFile

img_types = {
    b"\xff\xd8\xff\xdb": "jpeg",
    b"\xff\xd8\xff\xe0": "jpeg",
    b"\xff\xd8\xff\xee": "jpeg",
    b"\xff\xd8\xff\xe1": "jpeg",
    b"\x47\x49\x46\x38\x37\x61": "gif",
    b"\x47\x49\x46\x38\x39\x61": "gif",
    b"\x42\x4d": "bmp",
    b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": "png",
}


@auth_guard()
async def post_message_response_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Create message response
    tags:
        - message
    parameters:
        - in: path
          name: message_id
          required: true
          schema:
            type: integer
    responses:
        "200":
            description: Response created
            content:
                application/json:
                    schema:
                        type: integer
        "400":
            description: List of reasons<br/><br/>
                - path param message_id is too long<br/>
                - specify path param message_id<br/>
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
            description: Not found
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

    message_id = get_int_path_param(request, "message_id")

    try:
        parser = ImageFile.Parser()
        reader = await request.multipart()
        img_bytes = None
        img_data = None
        text = None
        media_type = None

        while part := await reader.next():
            if part.name == "file":
                img_data = await part.read()
            elif part.name == "text":
                text = (await part.read()).decode()

        if not img_data and not text:
            raise HTTPBadRequest(text="Пустой ответ")

        if img_data:
            parser.feed(img_data)

            img = parser.close()
            img.thumbnail((300, 300))

            for k, v in img_types.items():
                if img_data.startswith(k):
                    media_type = v
                    break

            img_bytes = BytesIO()
            img.save(img_bytes, format=media_type)
            img.close()

        message_id = await create_message_response(
            message_id, text, (img_bytes.getvalue() if img_bytes else None), media_type
        )
    except HTTPBadRequest as ex:
        raise ex
    except Exception:
        return HTTPBadRequest(text="Что-то пошло не так")

    return json_response(message_id)

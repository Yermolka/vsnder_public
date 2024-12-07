from io import BytesIO

from aiohttp.web import Request, json_response
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_session import get_session
from common.consts import USER_SESSION_USER_ID_KEY
from common.utils.auth import auth_guard
from modules.user.core.commands.create_log_entry import create_log_entry
from modules.user.core.commands.set_user_image_by_id import set_user_image_by_user_id
from modules.file.core.commands.create_file import create_file
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
async def post_user_image_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Upload avatar
    tags:
        - user
        - file
    responses:
        "200":
            description: ok
            content:
                application/json:
                    schema:
                        type: integer
        "400":
            description: Image is possibly broken
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
    
    session = await get_session(request)
    user_id = session[USER_SESSION_USER_ID_KEY]

    try:
        parser = ImageFile.Parser()
        reader = await request.multipart()
        while part := await reader.next():
            img_data = await part.read()
            break

        parser.feed(img_data)

        img = parser.close()
        img.thumbnail((300, 300))

        media_type = None
        for k, v in img_types.items():
            if img_data.startswith(k):
                media_type = v
                break

        img_bytes = BytesIO()
        img.save(img_bytes, format=media_type)
        img.close()

        file_id = await create_file(user_id, img_bytes.getvalue(), media_type)
    except Exception:
        raise HTTPBadRequest(text="Не удалось загрузить файл")
    
    await set_user_image_by_user_id(user_id, file_id)
    await create_log_entry(user_id, "image_upload")

    return json_response(user_id)

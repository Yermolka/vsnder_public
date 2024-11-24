from aiohttp.web import Request, Response
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_session import get_session

from io import BytesIO
from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from common.consts import USER_SESSION_USER_ID_KEY
from modules.message.core.commands.create_message import create_message
from PIL import ImageFile

img_types = {
    b'\xFF\xD8\xFF\xDB': 'jpeg',
    b'\xFF\xD8\xFF\xE0': 'jpeg',
    b'\xFF\xD8\xFF\xEE': 'jpeg',
    b'\xFF\xD8\xFF\xE1': 'jpeg',
    b'\x47\x49\x46\x38\x37\x61': 'gif',
    b'\x47\x49\x46\x38\x39\x61': 'gif',
    b'\x42\x4D': 'bmp',
    b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'png'
}


@auth_guard()
async def post_message_handler(request: Request):
    receiver_id = get_int_path_param(request, "receiver_id")
    session = await get_session(request)

    if int(session[USER_SESSION_USER_ID_KEY]) == receiver_id:
        return Response()

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

        await create_message(receiver_id, text, (img_bytes.getvalue() if img_bytes else None), media_type)
    except Exception as ex:
        return HTTPBadRequest(text=str(ex))

    return Response()

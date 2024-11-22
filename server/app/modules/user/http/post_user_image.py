from io import BytesIO
from aiohttp.web import Request, json_response
from aiohttp_session import get_session
from aiohttp.web_exceptions import HTTPBadRequest

from common.utils.auth import auth_guard
from common.consts import USER_SESSION_USER_ID_KEY
from modules.user.core.commands.set_user_image_by_id import set_user_image_by_user_id
from modules.user.core.commands.create_log_entry import create_log_entry
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
async def post_user_image_handler(request: Request):
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

        await set_user_image_by_user_id(user_id, img_bytes.getvalue(), media_type)
    
    except Exception as e:
        raise HTTPBadRequest(reason=str(e))
    
    await create_log_entry(user_id, "image_upload")

    return json_response(data={"user_id": user_id})

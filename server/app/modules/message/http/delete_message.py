from aiohttp.web import Request, json_response
from aiohttp_session import get_session

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from common.consts import USER_SESSION_USER_ID_KEY
from modules.message.core.commands.delete_message_by_id import delete_message_by_id


@auth_guard()
async def delete_message_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Delete message by it's id
    tags:
        - message
    parameters:
        - in: path
          name: id
          required: true
          schema:
            type: integer
    responses:
        "200":
            description: Message deleted
            content:
                application/json:
                    schema:
                        type: integer
        "400":
            description: List of reasons<br/><br/>
                - path param id is too long<br/>
                - specify path param id<br/>
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
            description: Message not found
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

    message_id = get_int_path_param(request, "id")

    await delete_message_by_id(user_id, message_id)

    return json_response(message_id)

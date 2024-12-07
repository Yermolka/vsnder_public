from aiohttp.web import Request, json_response

from common.utils.auth import auth_guard
from common.utils.http import get_int_path_param
from vsnder.dto.message import GetMessageDto
from modules.message.core.queries.get_public_messages_for_user_by_id import (
    get_public_messages_for_user_by_id
)


@auth_guard()
async def get_public_messages_handler(request: Request):
    """
    security:
        - cookieAuth: []
    description: Get public messages for user
    tags:
        - message
    parameters:
        - in: path
          name: receiver_id
          required: true
          schema:
            type: integer
    responses:
        "200":
            description: All messages for user
            content:
                application/json:
                    schema:
                        type: array
                        items:
                            $ref: "#/components/schemas/GetMessageDto"
        "400":
            description: List of reasons<br/><br/>
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
        "500":
            description: Internal server error
            content:
                text/plain:
                    schema:
                        type: string
    """

    receiver_id = get_int_path_param(request, "receiver_id")

    messages = await get_public_messages_for_user_by_id(receiver_id)

    return json_response(list(map(lambda m: GetMessageDto.from_model(m).to_dict(), messages)))

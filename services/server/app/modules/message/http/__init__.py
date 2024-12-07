from aiohttp import web

from .delete_message import delete_message_handler
from .get_messages import get_messages_handler
from .post_message import post_message_handler
from .post_message_response import post_message_response_handler
from .get_public_messages import get_public_messages_handler

message_routes = [
    web.get("/api/user/{receiver_id}/messages", get_messages_handler),
    web.get("/api/user/{receiver_id}/messages/public", get_public_messages_handler),
    web.post("/api/user/{receiver_id}/messages", post_message_handler),
    web.delete("/api/messages/{message_id}", delete_message_handler),
    web.post("/api/messages/{message_id}", post_message_response_handler),
]

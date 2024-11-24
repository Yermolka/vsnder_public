from aiohttp import web
from .get_messages import get_messages_handler
from .post_message import post_message_handler
from .delete_message import delete_message_handler
from .get_message_image import get_message_image_handler

message_routes = [
    web.get("/api/messages/{receiver_id}", get_messages_handler),
    web.post("/api/messages/{receiver_id}", post_message_handler),
    web.delete("/api/messages/{id}", delete_message_handler),
    web.get("/api/messages/{receiver_id}/{id}/file", get_message_image_handler),
]

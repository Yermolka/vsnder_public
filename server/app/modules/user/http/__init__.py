from aiohttp import web
from .post_login import user_login_handler

user_routes = [
    web.post("/api/user/login", user_login_handler),
]

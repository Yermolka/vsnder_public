from aiohttp import web
from .post_login import user_login_handler
from .get_logout import user_logout_handler
from .get_user import get_user_handler
from .get_users_page import get_users_page_handler
from .post_user import post_user_handler
from .post_change_password import post_change_password_handler
from .get_user_image import get_user_image_handler
from .post_user_image import post_user_image_handler
from .get_has_user_image import get_has_user_image_handler

user_routes = [
    web.post("/api/user/login", user_login_handler),
    web.get("/api/user/logout", user_logout_handler),
    web.get("/api/users/{user_id}", get_user_handler),
    web.get("/api/users", get_users_page_handler),
    web.post("/api/user/edit", post_user_handler),
    web.post("/api/user/change_password", post_change_password_handler),
    web.get("/api/users/{user_id}/file", get_user_image_handler),
    web.get("/api/users/{user_id}/file/has", get_has_user_image_handler),
    web.post("/api/users/{user_id}/file", post_user_image_handler),
]

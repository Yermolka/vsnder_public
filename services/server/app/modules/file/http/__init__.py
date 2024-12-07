from aiohttp import web

from .get_file import get_file_handler

file_routes = [
    web.get("/api/file/{file_id}", get_file_handler),
]

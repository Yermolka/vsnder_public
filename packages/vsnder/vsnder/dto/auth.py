from dataclasses import dataclass

from ..dto.base import DtoBase, SwaggerBase


@dataclass(kw_only=True)
class PostAuthDto(DtoBase, SwaggerBase):
    username: str
    password: str

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "username",
                "password",
            ],
            "properties": {
                "username": {
                    "type": "string",
                },
                "password": {
                    "type": "string",
                },
            },
        }

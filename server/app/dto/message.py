from dataclasses import dataclass

from dto.base import DtoBase, SwaggerBase
from models.message import Message


@dataclass(kw_only=True)
class PostMessageDto(DtoBase, SwaggerBase):
    file: bytes | None
    text: str | None

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "file": {"type": "string"},
            },
        }


@dataclass(kw_only=True)
class GetMessageDto(DtoBase, SwaggerBase):
    id: int
    text: str
    img_url: str | None

    @classmethod
    def from_model(cls, model: Message, receiver_id: int) -> "GetMessageDto":
        return cls(
            id=model.id,
            text=model.text,
            img_url=f"/api/messages/{receiver_id}/{model.id}/file"
            if model.has_picture
            else None,
        )

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "id",
                "text",
                "has_picture",
            ],
            "properties": {
                "id": {"typ": "integer"},
                "text": {"type": "string"},
                "img_url": {"type": "string"},
            },
        }


@dataclass(kw_only=True)
class NewPostMessageDto(DtoBase, SwaggerBase):
    text: str | None
    file: bytes | None
    sender_id: int | None
    public: bool

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "public",
            ],
            "properties": {
                "text": {"type": "string"},
                "file": {"type": "bytes"},
                "sender_id": {"type": "integer"},
                "public": {"type": "boolean"},
            },
        }


@dataclass(kw_only=True)
class NewPostMessageResponseDto(DtoBase, SwaggerBase):
    message_id: int
    text: str | None
    file: bytes | None

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "message_id",
            ],
            "properties": {
                "message_id": {"type": "integer"},
                "text": {"type": "string"},
                "file": {"type": "bytes"},
            },
        }


@dataclass(kw_only=True)
class NewGetMessageResponseDto(DtoBase, SwaggerBase):
    id: int
    text: str | None
    file_id: int | None

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "id",
            ],
            "properties": {
                "id": {"type": "integer"},
                "text": {"type": "string"},
                "file_id": {"type": "integer"},
            },
        }


@dataclass(kw_only=True)
class NewGetMessageDto(DtoBase, SwaggerBase):
    id: int
    text: str | None
    file_id: int | None
    response: NewGetMessageResponseDto | None
    public: bool

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "id",
                "public",
            ],
            "properties": {
                "id": {"type": "integer"},
                "text": {"type": "string"},
                "file_id": {"type": "integer"},
                "response": {
                    "$ref": "#/components/schemas/NewGetMessageResponseDto",
                },
                "public": {"type": "boolean"},
            },
        }

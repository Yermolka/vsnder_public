from dataclasses import dataclass

from ..dto.base import DtoBase, SwaggerBase
from ..models.message import Message


@dataclass(kw_only=True)
class PostMessageDto(DtoBase, SwaggerBase):
    text: str | None
    file: bytes | None
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
                "public": {"type": "boolean"},
            },
        }


@dataclass(kw_only=True)
class PostMessageResponseDto(DtoBase, SwaggerBase):
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
class GetMessageDto(DtoBase, SwaggerBase):
    id: int
    text: str | None
    file_id: int | None
    answer_text: str | None
    answer_file_id: int | None
    public: bool

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "id",
                "text",
                "file_id",
                "answer_text",
                "answer_file_id",
                "public",
            ],
            "properties": {
                "id": {"type": "integer"},
                "text": {"type": "string"},
                "file_id": {"type": "integer"},
                "answer_text": {"type": "string"},
                "answer_file_id": {"type": "integer"},
                "public": {"type": "boolean"},
            },
        }

    @classmethod
    def from_model(cls, model: Message) -> "GetMessageDto":
        return cls(
            id=model.id,
            text=model.text,
            file_id=model.file_id,
            answer_text=model.answer_text,
            answer_file_id=model.answer_file_id,
            public=model.public,
        )

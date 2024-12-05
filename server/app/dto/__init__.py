from .auth import PostAuthDto
from .user import GetUserDto, GetShortUserDto, PostUserDto
from .message import (
    GetMessageDto,
    PostMessageDto,
    NewGetMessageDto,
    NewGetMessageResponseDto,
    NewPostMessageDto,
    NewPostMessageResponseDto,
)

all_dtos = [
    PostAuthDto,
    GetUserDto,
    GetShortUserDto,
    PostUserDto,
    GetMessageDto,
    PostMessageDto,
    NewGetMessageDto,
    NewGetMessageResponseDto,
    NewPostMessageDto,
    NewPostMessageResponseDto,
]

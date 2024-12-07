from .auth import PostAuthDto
from .message import GetMessageDto, PostMessageDto, PostMessageResponseDto
from .user import GetShortUserDto, GetUserDto, PostUserDto

all_dtos = [
    PostAuthDto,
    GetMessageDto,
    PostMessageDto,
    PostMessageResponseDto,
    GetShortUserDto,
    GetUserDto,
    PostUserDto,
]

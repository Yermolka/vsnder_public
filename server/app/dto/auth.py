from dataclasses import dataclass

from dto.base import DtoBase

@dataclass(kw_only=True)
class PostAuthDto(DtoBase):
    username: str
    password: str

from dataclasses import dataclass

@dataclass(kw_only=True)
class Message:
    id: int
    text: str
    has_picture: bool

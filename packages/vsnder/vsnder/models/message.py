from dataclasses import dataclass

@dataclass(kw_only=True)
class Message:
    id: int
    receiver_id: int
    text: str | None
    file_id: int | None
    answer_text: str | None
    answer_file_id: int | None
    public: bool

from dto.base import DtoBase
from dataclasses import dataclass

from models.user import User


@dataclass(kw_only=True)
class GetUserDto(DtoBase):
    id: int
    username: str
    age: int
    orientation: str


    @classmethod
    def from_model(cls, model: User) -> "GetUserDto":
        return cls(
            id=model.id,
            username=model.username,
            age=model.age,
            orientation=model.orientation or "",
        )


@dataclass(kw_only=True)
class PostUserDto(DtoBase):
    age: int
    orientation: str | None = None
    interests: str | None = None
    vsn_interests: str | None = None
    places_to_visit: str | None = None
    study_places: str | None = None
    music: str | None = None
    favorite_movies: str | None = None
    religion: str | None = None
    status: str | None = None
    future_plans: str | None = None
    family_opinion: str | None = None
    favorite_programming_language: str | None = None
    lizards_or_russians: bool = True
    smoking: str | None = None
    top_3_people: str | None = None
    drinking: str | None = None

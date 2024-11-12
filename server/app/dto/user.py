from dto.base import DtoBase
from dataclasses import dataclass
from typing import Literal

from models.user import User


@dataclass(kw_only=True)
class GetShortUserDto(DtoBase):
    id: int
    first_name: str
    last_name: str
    orientation: str
    year_of_study: int
    has_avatar: bool

    @classmethod
    def from_model(cls, model: User) -> "GetShortUserDto":
        return cls(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            orientation=model.orientation,
            year_of_study=model.year_of_study,
            has_avatar=model.has_avatar,
        )


@dataclass(kw_only=True)
class GetUserDto(DtoBase):
    id: int
    first_name: str
    last_name: str
    age: int | None
    year_of_study: int
    orientation: str
    interests: str
    vsn_interests: str
    places_to_visit: str
    study_places: str
    music: str
    favorite_movies: str
    religion: str
    status: str
    future_plans: str
    family_opinion: str
    favorite_programming_language: str
    lizards_or_russians: bool = True
    smoking: str
    top_3_people: str
    drinking: str
    has_avatar: bool

    @classmethod
    def from_model(cls, model: User) -> "GetUserDto":
        return cls(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            age=model.age or None,
            year_of_study=model.year_of_study,
            orientation=model.orientation or "",
            interests=model.interests or "",
            vsn_interests=model.vsn_interests or "",
            places_to_visit=model.places_to_visit or "",
            study_places=model.study_places or "",
            music=model.music or "",
            favorite_movies=model.favorite_movies or "",
            religion=model.religion or "",
            status=model.status or "",
            future_plans=model.future_plans or "",
            family_opinion=model.family_opinion or "",
            favorite_programming_language=model.favorite_programming_language or "",
            lizards_or_russians=model.lizards_or_russians,
            smoking=model.smoking or "",
            top_3_people=model.top_3_people or "",
            drinking=model.drinking or "",
            has_avatar=model.has_avatar,
        )


@dataclass(kw_only=True)
class PostUserDto(DtoBase):
    age: int | None = None
    year_of_study: int
    orientation: Literal["Социология", "Психология", "Политология", "ГМУ"] | None = None
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
    smoking: Literal["Положительно", "Отрицательно", "Нейтрально"] | None = None
    top_3_people: str | None = None
    drinking: Literal["Положительно", "Отрицательно", "Нейтрально"] | None = None

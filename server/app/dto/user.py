from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from dto.base import DtoBase, SwaggerBase
from models.user import User


@dataclass(kw_only=True)
class GetShortUserDto(DtoBase, SwaggerBase):
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
    
    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "id",
                "first_name",
                "last_name",
                "orientation",
                "year_of_study",
                "has_avatar",
            ],
            "properties": {
                "id": {
                    "type": "integer",
                },
                "first_name": {
                    "type": "string",
                },
                "last_name": {
                    "type": "string",
                },
                "orientation": {
                    "type": "string",
                },
                "year_of_study": {
                    "type": "integer",
                },
                "has_avatar": {
                    "type": "boolean",
                }
            }
        }


@dataclass(kw_only=True)
class GetUserDto(DtoBase, SwaggerBase):
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
    birth_stamp: str
    birth_city: str

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
            birth_stamp=model.birth_stamp.isoformat() if model.birth_stamp else "",
            birth_city=model.birth_city or "",
        )
    
    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "id",
                "first_name",
                "last_name",
                "year_of_study",
                "orientation",
                "interests",
                "vsn_interests",
                "places_to_visit",
                "study_places",
                "music",
                "favorite_movies",
                "religion",
                "status",
                "future_plans",
                "family_opinion",
                "favorite_programming_language",
                "lizards_or_russians",
                "smoking",
                "top_3_people",
                "drinking",
                "has_avatar",
                "birth_stamp",
                "birth_city",
            ],
            "properties": {
                "id": {"type": "integer"},
                "first_name": {"type": "string"},
                "last_name": {"type": "string"},
                "age": {"type": "integer"},
                "year_of_study": {"type": "integer"},
                "orientation": {"type": "string"},
                "interests": {"type": "string"},
                "vsn_interests": {"type": "string"},
                "places_to_visit": {"type": "string"},
                "study_places": {"type": "string"},
                "music": {"type": "string"},
                "favorite_movies": {"type": "string"},
                "religion": {"type": "string"},
                "status": {"type": "string"},
                "future_plans": {"type": "string"},
                "family_opinion": {"type": "string"},
                "favorite_programming_language": {"type": "string"},
                "lizards_or_russians": {"type": "boolean"},
                "smoking": {"type": "string"},
                "top_3_people": {"type": "string"},
                "drinking": {"type": "string"},
                "has_avatar": {"type": "boolean"},
                "birth_stamp": {"type": "string"},
                "birth_city": {"type": "string"},
            }
        }


@dataclass(kw_only=True)
class PostUserDto(DtoBase, SwaggerBase):
    age: int | None = field(metadata={"deserialize": lambda x: x or None})
    year_of_study: int
    orientation: Literal["Социология", "Психология", "Политология", "ГМУ"] | None = (
        field(metadata={"deserialize": lambda x: x or None})
    )
    interests: str | None = field(metadata={"deserialize": lambda x: x or None})
    vsn_interests: str | None = field(metadata={"deserialize": lambda x: x or None})
    places_to_visit: str | None = field(metadata={"deserialize": lambda x: x or None})
    study_places: str | None = field(metadata={"deserialize": lambda x: x or None})
    music: str | None = field(metadata={"deserialize": lambda x: x or None})
    favorite_movies: str | None = field(metadata={"deserialize": lambda x: x or None})
    religion: str | None = field(metadata={"deserialize": lambda x: x or None})
    status: (
        Literal["Замужем/Женат", "В отношениях", "Схожу на свидание", "Чиллю соло"]
        | None
    ) = field(metadata={"deserialize": lambda x: x or None})
    future_plans: str | None = field(metadata={"deserialize": lambda x: x or None})
    family_opinion: str | None = field(metadata={"deserialize": lambda x: x or None})
    favorite_programming_language: str | None = field(
        metadata={"deserialize": lambda x: x or None}
    )
    lizards_or_russians: bool = True
    smoking: Literal["Положительно", "Отрицательно", "Нейтрально"] | None = field(
        metadata={"deserialize": lambda x: x or None}
    )
    top_3_people: str | None = field(metadata={"deserialize": lambda x: x or None})
    drinking: Literal["Положительно", "Отрицательно", "Нейтрально"] | None = field(
        metadata={"deserialize": lambda x: x or None}
    )
    birth_stamp: datetime | None = field(
        metadata={"deserialize": lambda x: datetime.fromisoformat(x) if x else None}
    )
    birth_city: str | None = field(metadata={"deserialize": lambda x: x or None})

    @staticmethod
    def swagger():
        return {
            "type": "object",
            "required": [
                "year_of_study",
                "lizard_or_russians",
            ],
            "properties": {
                "age": {"type": "integer"},
                "year_of_study": {"type": "integer"},
                "orientation": {"type": "string", "oneOf": ["Социология", "Психология", "Политология", "ГМУ"]},
                "interests": {"type": "string"},
                "vsn_interests": {"type": "string"},
                "places_to_visit": {"type": "string"},
                "study_places": {"type": "string"},
                "music": {"type": "string"},
                "favorite_movies": {"type": "string"},
                "religion": {"type": "string"},
                "status": {"type": "string", "oneOf": ["Замужем/Женат", "В отношениях", "Схожу на свидание", "Чиллю соло"]},
                "future_plans": {"type": "string"},
                "family_opinion": {"type": "string"},
                "favorite_programming_language": {"type": "string"},
                "lizards_or_russians": {"type": "boolean"},
                "smoking": {"type": "string", "oneOf": ["Положительно", "Отрицательно", "Нейтрально"]},
                "top_3_people": {"type": "string"},
                "drinking": {"type": "string", "oneOf": ["Положительно", "Отрицательно", "Нейтрально"]},
                "birth_stamp": {"type": "string", "format": "date-time"},
                "birth_city": {"type": "string"},
            }
        }

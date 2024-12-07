from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal

from ..dto.base import DtoBase, SwaggerBase
from ..models.user import User


@dataclass(kw_only=True)
class GetShortUserDto(DtoBase, SwaggerBase):
    id: int
    first_name: str
    last_name: str
    orientation: str
    year_of_study: int
    file_id: int

    @classmethod
    def from_model(cls, model: User) -> "GetShortUserDto":
        return cls(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            orientation=model.orientation,
            year_of_study=model.year_of_study,
            file_id=model.file_id,
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
    year_of_study: int | None
    orientation: str | None
    interests: str | None
    vsn_interests: str | None
    places_to_visit: str | None
    study_places: str | None
    music: str | None
    favorite_movies: str | None
    religion: str | None
    status: str | None
    future_plans: str | None
    family_opinion: str | None
    favorite_programming_language: str | None
    lizards_or_russians: bool = True
    smoking: str | None
    top_3_people: str | None
    drinking: str | None
    file_id: int | None
    birth_stamp: str | None
    birth_city: str | None

    @classmethod
    def from_model(cls, model: User) -> "GetUserDto":
        return cls(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            age=model.age,
            year_of_study=model.year_of_study,
            orientation=model.orientation,
            interests=model.interests,
            vsn_interests=model.vsn_interests,
            places_to_visit=model.places_to_visit,
            study_places=model.study_places,
            music=model.music,
            favorite_movies=model.favorite_movies,
            religion=model.religion,
            status=model.status,
            future_plans=model.future_plans,
            family_opinion=model.family_opinion,
            favorite_programming_language=model.favorite_programming_language,
            lizards_or_russians=model.lizards_or_russians,
            smoking=model.smoking,
            top_3_people=model.top_3_people,
            drinking=model.drinking,
            file_id=model.file_id,
            birth_stamp=model.birth_stamp.isoformat() if model.birth_stamp else None,
            birth_city=model.birth_city,
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
                "file_id",
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
                "file_id": {"type": "integer"},
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

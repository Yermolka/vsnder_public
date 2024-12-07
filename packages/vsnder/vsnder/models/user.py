from dataclasses import dataclass
from datetime import datetime

@dataclass(kw_only=True)
class User:
    id: int
    username: str
    first_name: str
    last_name: str
    password_hash: str
    original_password: str
    age: int | None = None
    year_of_study: int
    orientation: str | None = None
    interests: str | None = None
    vsn_interests: str | None = None
    study_places: str | None = None
    music: str | None = None
    favorite_movies: str | None = None
    religion: str | None = None
    status: str | None = None
    future_plans: str | None = None
    family_opinion: str | None = None
    favorite_programming_language: str | None = None
    lizards_or_russians: str | None = "on"
    smoking: str | None = None
    top_3_people: str | None = None
    drinking: str | None = None
    places_to_visit: str | None = None
    created: datetime
    modified: datetime
    file_id: int | None = None
    birth_stamp: datetime | None = None
    birth_city: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(**data)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "original_password": self.original_password,
            "password_hash": self.password_hash,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "year_of_study": self.year_of_study,
            "orientation": self.orientation,
            "interests": self.interests,
            "vsn_interests": self.vsn_interests,
            "study_places": self.study_places,
            "music": self.music,
            "favorite_movies": self.favorite_movies,
            "religion": self.religion,
            "status": self.status,
            "future_plans": self.future_plans,
            "family_opinion": self.family_opinion,
            "favorite_programming_language": self.favorite_programming_language,
            "lizards_or_russians": self.lizards_or_russians,
            "smoking": self.smoking,
            "top_3_people": self.top_3_people,
            "drinking": self.drinking,
            "places_to_visit": self.places_to_visit,
            "created": self.created.timestamp(),
            "modified": self.modified.timestamp(),
            "file_id": self.file_id,
            "birth_stamp": self.birth_stamp.timestamp(),
            "birth_city": self.birth_city,
        }

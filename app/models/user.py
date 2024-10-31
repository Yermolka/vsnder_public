from dataclasses import dataclass


@dataclass(kw_only=True)
class User:
    id: int
    username: str
    password: str | None = None
    original_password: str | None = None
    age: int | None = None
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

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(**data)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "age": self.age,
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
        }


@dataclass(kw_only=True)
class PutUserDto:
    username: str
    age: int | None = None
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
    lizards_or_russians: str | None = None
    smoking: str | None = None
    top_3_people: str | None = None
    drinking: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(**data)

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "age": self.age,
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
        }

from abc import ABC, abstractmethod

from mashumaro.mixins.json import DataClassJSONMixin


class DtoBase(DataClassJSONMixin):
    pass


class SwaggerBase(ABC):
    @staticmethod
    @abstractmethod
    def swagger() -> dict:
        pass

    @staticmethod
    def swagger_ref(entity: type):
        return f"#/components/schemas/{entity.__name__}"

import json
from typing import Generic, List, Optional, TypeVar
import swibots
from swibots.utils.types import JSONDict


T = TypeVar("T")


class SwitchObject(Generic[T]):
    def __init__(self, app: "swibots.App" = None, **kwargs):
        self._app = app
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def app(self) -> "swibots.App":
        return self._app

    @classmethod
    def build_from_json(
        cls, data: Optional[JSONDict] = None, app: Optional["swibots.App"] = None
    ) -> Optional[T]:
        if data is None:
            return None
        return cls(app).from_json(data)

    @classmethod
    def build_from_json_list(
        cls, data: Optional[JSONDict], app: Optional["swibots.App"] = None
    ) -> List[T]:
        return [cls.build_from_json(item, app) for item in data]

    def to_json_request(self) -> JSONDict:
        return self.to_json()

    def to_json(self) -> JSONDict:
        return self.__dict__

    def from_json(self, data: Optional[JSONDict]) -> T:
        for key, value in data.items():
            setattr(self, key, value)
        return self

    def prettify(self, indent_count: int = 1) -> str:
        result = f"{self.__class__.__name__}"
        result += " {\n"

        def parseList(data, indent=2):
            if not data:
                return "[]"
            result = "["
            return result

        print(self.__dict__)
        for key, value in self.__dict__.items():
            if value is None:
                continue
            result += (" " * indent_count * 2) + f'"{key}": '
            if hasattr(value, "prettify"):
                indent_count += 1
                value = value.prettify(indent_count * 2)
            elif isinstance(value, str):
                value = f'"{value}"'
            elif isinstance(value, list):
                value += parseList(value, indent_count + 1 * 2)
            else:
                value = str(value)
            result += f"{value}\n"
        result += "}"
        return result

    def __repr__(self) -> str:
        return json.dumps(self.to_json(), indent=1)
        def parseObject(obj: SwitchObject):
            return {
                x: parseValue(y) for x, y in obj.__dict__.items() if y and x != "_app"
            }

        def parseValue(value):
    
            if isinstance(value, SwitchObject):
                return parseObject(value)
            elif isinstance(value, list):
                return list(map(parseValue, value))
            return value

        filter_dict = parseObject(self)
        return f"{self.__class__.__name__} {json.dumps(filter_dict, indent=1)}"

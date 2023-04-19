import enum
from typing import Dict, List


class LanguagesEnum(str, enum.Enum):
    en = "🇺🇸 EN"
    ru = "🇷🇺 РУ"

    @classmethod
    def get_names(cls) -> List[str]:
        return [el.name for el in cls]

    @classmethod
    def get_values(cls) -> List[str]:
        return [el.name for el in cls]

    @classmethod
    def get_names_and_values(cls, reverse: bool = False) -> Dict[str, str]:
        names_and_values = {}
        for el in cls:
            if reverse:
                names_and_values[el.value] = el.name
            else:
                names_and_values[el.name] = el.value

        return names_and_values

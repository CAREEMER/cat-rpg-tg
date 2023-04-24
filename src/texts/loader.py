from typing import List

from .languages import LanguagesEnum


class BaseTextsContainer:
    chosen_language = ""
    menu = ""
    enter_dungeon = ""
    settings = ""
    choose_settings_option = ""
    language = ""


class RuTextContainer:
    chosen_language = "Вы установили русский язык!"
    menu = "Выберите активность:"
    enter_dungeon = "Войти в подземелье"
    settings = "Настройки"
    choose_settings_option = "Выберите опцию настроек:"
    language = "Выбрать язык"


class EnTextContainer:
    chosen_language = "You have chosen english language!"
    menu = "Choose an activity:"
    enter_dungeon = "Enter the dungeon"
    settings = "Settings"
    choose_settings_option = "Choose settings option:"
    language = "Choose a language"


LANGS = {
    LanguagesEnum.en.name: EnTextContainer,
    LanguagesEnum.ru.name: RuTextContainer,
}


def _get_class_attributes(cls) -> List[str]:
    output_list = []

    for attribute in cls.__dict__.keys():
        if not attribute.startswith("__"):
            value = getattr(cls, attribute)
            if not callable(value):
                if not isinstance(value, str):
                    raise ValueError
                output_list.append(attribute)

    return output_list


def validate_translation_completeness() -> None:
    containers_to_validate = list(LANGS.values())
    complete_attrs = _get_class_attributes(BaseTextsContainer)

    for container in containers_to_validate:
        if not _get_class_attributes(container) == complete_attrs:
            raise ValueError

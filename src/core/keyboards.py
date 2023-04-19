from typing import Dict, List, Tuple, Union

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from services.message import generate_imessage_id
from texts.languages import LanguagesEnum


def construct_keyboard(names: list, callbacks: list = None):
    if not callbacks:
        buttons = [InlineKeyboardButton(name, callback_data=str(idx + 1)) for idx, name in enumerate(names)]
    else:
        buttons = [
            InlineKeyboardButton(name, callback_data=str(idx)) for idx, name in dict(zip(callbacks, names)).items()
        ]

    inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    [inline_keyboard.add(button) for button in buttons]

    return inline_keyboard


def construct_keyboard_from_dict(names_and_callbacks: Dict[str, str]):
    buttons = []
    for name, callback in names_and_callbacks.items():
        buttons.append(InlineKeyboardButton(name, callback_data=callback))

    inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    inline_keyboard.add(*buttons)

    return inline_keyboard


def construct_language_codes_keyboard() -> Tuple[InlineKeyboardMarkup, List[Dict[str, Union[str, int]]]]:
    names_and_values = LanguagesEnum.get_names_and_values(reverse=True)
    reply_markup_message_data = []

    for name, value in names_and_values.items():
        imessage_id = generate_imessage_id()
        reply_markup_message_data.append({"language_code": value, "pk": imessage_id})

        names_and_values[name] = f"lan_{imessage_id}"

    return construct_keyboard_from_dict(names_and_values), reply_markup_message_data

from typing import Tuple

from aiogram.types import InlineKeyboardMarkup

from models import User
from core.keyboards import construct_keyboard
from texts.loader import LANGS
from core.enums import InlineButtonCallbackQueryEnum


def get_settings_message(user: User) -> Tuple[str, InlineKeyboardMarkup]:
    text_container = LANGS.get(user.language)
    keyboard = construct_keyboard([text_container.language], [InlineButtonCallbackQueryEnum.language.name])

    return text_container.choose_settings_option, keyboard

from typing import Tuple

from aiogram.types import InlineKeyboardMarkup

from core.enums import InlineButtonCallbackQueryEnum
from core.keyboards import construct_keyboard
from models import User
from texts.loader import LANGS


def get_menu_text_and_keyboard(user: User) -> Tuple[str, InlineKeyboardMarkup]:
    text_container = LANGS.get(user.language)
    keyboard = construct_keyboard(
        [text_container.enter_dungeon, text_container.settings],
        [InlineButtonCallbackQueryEnum.enter_dungeon.name, InlineButtonCallbackQueryEnum.settings.name],
    )
    return text_container.menu, keyboard

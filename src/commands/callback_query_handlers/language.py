from aiogram import types

from core import dp
from services.user import get_user
from texts.languages import LanguagesEnum
from texts.loader import LANGS


@dp.callback_query_handler(lambda c: c.data.startswith("lan_"))
async def process_language_choosing(callback_query: types.CallbackQuery):
    chosen_language = callback_query.data.split("_")[1]
    if chosen_language not in [lan.name for lan in LanguagesEnum]:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text=f"Язык {chosen_language} не поддерживается."
        )

    user = get_user(callback_query.from_user)
    user.language = chosen_language
    user.update()

    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id, text=LANGS.get(user.language).chosen_language
    )

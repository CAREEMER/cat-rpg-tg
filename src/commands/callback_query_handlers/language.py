import json

from aiogram import types

from core import dp
from core.utils import parse_params
from services.message import get_reply_markup_message
from services.user import get_user
from texts.languages import LanguagesEnum
from texts.loader import LANGS


@dp.callback_query_handler(lambda c: c.data.startswith("lan_"))
async def process_language_choosing(callback_query: types.CallbackQuery):
    imessage_id = callback_query.data.split("_")[-1]
    reply_markup_message = await get_reply_markup_message(imessage_id)

    if reply_markup_message.language_code not in LanguagesEnum.get_names():
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text=f"Язык {reply_markup_message.language_code} не поддерживается."
        )

    user = get_user(callback_query.from_user)
    user.language = reply_markup_message.language_code
    user.update()

    await callback_query.bot.edit_message_reply_markup(
        chat_id=callback_query.from_user.id,
        message_id=reply_markup_message.message_id,
        reply_markup=None,
    )

    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id, text=LANGS.get(user.language).chosen_language
    )

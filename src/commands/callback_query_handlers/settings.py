from aiogram import types

from core import dp
from core.enums import InlineButtonCallbackQueryEnum
from services.messages.settings import get_settings_message
from services.user import get_user


@dp.callback_query_handler(lambda c: c.data == InlineButtonCallbackQueryEnum.settings.name)
async def process_settings(callback_query: types.CallbackQuery):
    user = get_user(callback_query.from_user)
    text, keyboard = get_settings_message(user)
    await callback_query.bot.send_message(callback_query.from_user.id, text, reply_markup=keyboard)

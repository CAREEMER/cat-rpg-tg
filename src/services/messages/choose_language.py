from aiogram import types

from core.keyboards import construct_language_codes_keyboard
from models import User
from services.reply_markup_message import bulk_create_reply_markup_message


async def send_choose_language_message(user: User, message: types.Message = None, callback_query: types.CallbackQuery = None):
    keyboard, reply_markup_message_objects_data = construct_language_codes_keyboard()
    bot = message.bot if message else callback_query.bot
    chat_id = message.from_user.id if message else callback_query.from_user.id
    message = await bot.send_message(
        chat_id,
        f"Hello, {user.verbose_name}! Choose the language!\n\nПривет, {user.verbose_name}! Выбери язык!",
        reply_markup=keyboard,
    )
    for obj in reply_markup_message_objects_data:
        obj["message_id"] = message.message_id

    await bulk_create_reply_markup_message(reply_markup_message_objects_data)

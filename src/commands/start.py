from aiogram import types

from core import dp
from core.keyboards import construct_language_codes_keyboard
from services.message import bulk_create_reply_markup_message


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    credentials = message.from_user.username if message.from_user.username else message.from_user.first_name

    keyboard, reply_markup_message_objects_data = construct_language_codes_keyboard()
    message = await message.reply(
        f"Hello, {credentials}! Choose the language!\n\nПривет, {credentials}! Выбери язык!", reply_markup=keyboard
    )
    for obj in reply_markup_message_objects_data:
        obj["message_id"] = message.message_id

    await bulk_create_reply_markup_message(reply_markup_message_objects_data)

from aiogram import types

from core import dp
from services.messages.choose_language import send_choose_language_message
from services.messages.menu import get_menu_text_and_keyboard


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message, user):
    if not user.language:
        await send_choose_language_message(user, message=message)
    else:
        text, keyboard = get_menu_text_and_keyboard(user)
        await message.bot.send_message(message.from_user.id, text, reply_markup=keyboard)

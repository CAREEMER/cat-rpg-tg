from aiogram import types

from core import dp, construct_keyboard


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    credentials = message.from_user.username if message.from_user.username else message.from_user.first_name
    keyboard = construct_keyboard(["🇺🇸 EN", "🇷🇺 РУ"], ["lan_en", "lan_ru"])
    await message.reply(f"Hello, {credentials}! Choose the language!\n\nПривет, {credentials}! Выбери язык!", reply_markup=keyboard)

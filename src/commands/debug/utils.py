import datetime

from aiogram import types

from core import dp
from core.utils import admin_command


@dp.message_handler(commands=["debug"])
@admin_command()
async def process_debug_command(message: types.Message):
    await message.reply(f"datetime - {datetime.datetime.now()}\ndate - {datetime.date.today()}")


@dp.message_handler(commands=["timer"])
@admin_command()
async def process_timer_command(message: types.Message):
    import asyncio

    timer = 10
    reply_message = await message.reply(str(timer))

    while timer != 0:
        timer -= 1
        await asyncio.sleep(1)
        await reply_message.edit_text(str(timer))

    await reply_message.delete()

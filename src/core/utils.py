import asyncio
import functools

from aiogram import types


async def delete_after(message: types.Message, delay: int = 10):
    await asyncio.sleep(delay)
    await message.delete()


def admin_command():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(message: types.Message, *args, **kwargs):
            if not message.from_user.id == 123121982:
                return

            await func(message, *args, **kwargs)

        return wrapped

    return wrapper


def private_command():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(message: types.Message, *args, **kwargs):
            if not message.from_user.id == message.chat.id:
                reply_message = await message.reply(
                    "Эту команду можно использовать только в личных сообщениях с ботом!"
                )
                await delete_after(reply_message, 3)
                return

            await func(message, *args, **kwargs)

        return wrapped

    return wrapper


def private_admin_command():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(message: types.Message, *args, **kwargs):
            if not message.chat.id == 123121982:
                return

            await func(message, *args, **kwargs)

        return wrapped

    return wrapper

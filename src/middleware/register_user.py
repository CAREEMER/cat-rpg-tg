from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from services.user import get_or_create_user


class RegisterUserMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        data["user"] = get_or_create_user(message.from_user)

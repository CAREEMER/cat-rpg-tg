from typing import Union

from aiogram import types

from models import User


def get_user(user_data: types.User) -> Union[User, None]:
    user = User.get_obj(User.id == str(user_data.id))
    if not user:
        return

    if any(
        (user.full_name != user_data.full_name, user.username != user_data.username, user.mention != user_data.mention)
    ):
        user.full_name = user_data.full_name
        user.username = user_data.username
        user.mention = user_data.mention

        user.update()

    return user


def create_user(user_data: types.User) -> User:
    return User.create_obj(id=user_data.id, username=user_data.username, mention=user_data.mention)


def get_or_create_user(user_data: types.User) -> User:
    return get_user(user_data) or create_user(user_data)

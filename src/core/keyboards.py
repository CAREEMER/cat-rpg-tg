from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def construct_keyboard(names: list, callbacks: list = None):
    if not callbacks:
        buttons = [InlineKeyboardButton(name, callback_data=str(idx + 1)) for idx, name in enumerate(names)]
    else:
        buttons = [
            InlineKeyboardButton(name, callback_data=str(idx)) for idx, name in dict(zip(callbacks, names)).items()
        ]

    inline_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    [inline_keyboard.add(button) for button in buttons]

    return inline_keyboard

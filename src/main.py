from aiogram import executor

import commands  # NOQA
from core import dp, settings
from middleware.register_user import RegisterUserMiddleware
from texts.loader import validate_translation_completeness


def main():
    dp.middleware.setup(RegisterUserMiddleware())
    executor.start_polling(dp, skip_updates=settings.LOCAL)


if __name__ == "__main__":
    validate_translation_completeness()
    main()

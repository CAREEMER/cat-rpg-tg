from aiogram.dispatcher.filters.state import State, StatesGroup


class HelloWorldState(StatesGroup):
    file = State()

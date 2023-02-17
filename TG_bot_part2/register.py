from telebot.handler_backends import State, StatesGroup


class StudentRegisterForm(StatesGroup):
    name = State()
    surname = State()
    age = State()
    city = State()
    contact = State()
    language = State()
    course = State()

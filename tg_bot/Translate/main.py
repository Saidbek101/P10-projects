import telebot
from environs import Env
from datetime import datetime

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from translate import Translator

env = Env()
env.read_env()

BOT_TOKEN = env("BOT_TOKEN")
pink_translate_bot = telebot.TeleBot(BOT_TOKEN)

country = {'uzbek': 'uz', 'turkey': 'tk', "ukraine": "ug", 'korea': "ko"}

a = []


# Keyboard
def key_button():
    login_or_sign = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in country:
        login_or_sign.add(KeyboardButton(i))
    return login_or_sign


# Star message
@pink_translate_bot.message_handler(commands=["start"])
def star_message(message):
    pink_translate_bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}", reply_markup=key_button())
    pink_translate_bot.register_next_step_handler(message, get_message)


@pink_translate_bot.message_handler(chat_types=['text'])
def get_message(message):
    try:
        Translator(to_lang=str(country.get(message.text)))
    except NameError:
        pink_translate_bot.send_message(message.chat.id, f"Some error")
    else:
        pink_translate_bot.send_message(message.chat.id, f"Ok enter text:")
        a.append(country.get(message.text))



if __name__ == '__main__':
    pink_translate_bot.infinity_polling()

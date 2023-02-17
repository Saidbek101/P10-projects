from datetime import datetime
from environs import Env
import telebot
from telebot.types import BotCommand

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


# Start
@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    answer = f'Hello {user.first_name}' \
             f' Welcome calculate age'
    bot.reply_to(message, answer)


@bot.message_handler(commands=['age'])
def age(message):
    msg = bot.reply_to(message, 'Enter your birth year' '🥳')
    bot.register_next_step_handler(msg, age_func)


def age_func(message):
    present_year = int(datetime.now().strftime('%Y'))
    try:
        user_year = int(message.text)
    except Exception as e:
        answer = "Enter your birth year"
        bot.reply_to(message, answer)
    else:
        if user_year < present_year:
            text = f"He {present_year - user_year} year old"
            bot.reply_to(message, text)
        else:
            answer = "😡 Please enter your birth year correctly 😡"
            bot.reply_to(message, answer)


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/age", "Age bot")
    ]


if __name__ == "__main__":
    print("Worked...")
    bot.set_my_commands(commands=my_commands())
    bot.polling()

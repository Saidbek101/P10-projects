import json
# import requests
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
             f' Welcome'
    bot.reply_to(message, answer)


@bot.message_handler(commands=['currency'])
def get_valut(message):
    answer = 'Enter the currency: '
    msg = bot.reply_to(message, answer)
    bot.register_next_step_handler(msg, convert)


currency = ['UZS']


def convert(message):
    import requests

    money_1 = message
    money_2 = message
    amount = 5

    url = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'
    headers = {
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com",
        "x-rapidapi-key": "91d8898136msh83f56071c8737b2p1cbab2jsn4413d1661d85"
    }
    response = requests.request('GET', url, headers=headers)
    data = json.loads(response.text)

    for i in data:
        if i['Ssu'] == money_1 and money_2 == 'UZS':
            float_value = float(i['Cost'])
            amount = float(amount)
            return float_value * amount
        elif i['Ssu'] == money_2 and money_1 == 'UZS':
            float_value = float(i['Cost'])
            amount = float(amount)
            return amount / float_value
        elif money_1 == i['Ssu']:
            for a in data:
                if money_2 == a['Ssu']:
                    first_value = float(i["Cost"])
                    second_value = float(a["Cost"])
                    return first_value / second_value
        else:
            if money_1 == "UZS" and money_2 == "UZS":
                return float(amount)


def my_commands():
    return [
        BotCommand('/start', 'Start bot'),
        BotCommand('/currency', 'Currency convert bot')
    ]


if __name__ == '__main__':
    print('Worked...')
    bot.set_my_commands(commands=my_commands())
    bot.polling()

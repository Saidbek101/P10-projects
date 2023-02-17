import telebot
import requests
import json

api_token = '6158172522:AAGh2ZzMUsf1inAgcwmLYY6vdkMjYyLPJWA'

url = "https://api.weather.yandex.ru/v2/informers?lat=55.75222&lon=37.61556"
headers = {"X-Yandex-API-Key": "52fa68c1-1f34-43ed-a8fa-6bc98eb34b31"}

bot = telebot.TeleBot(api_token)


@bot.message_handler(commands=['start'])
def get_weather(message):
    bot.send_message(message.chat.id, text=f'Hello,\
    {message.from_user.username}!\
    \n\nI can show you the weather with:\
    \n/weather\n/pogoda\n/get_weather')


@bot.message_handler(commands=['get_weather', 'weather', 'pogoda'])
def get_weather(message):
    r = requests.get(url=url, headers=headers)
    bot.send_message(message.chat.id, r.text)
    if r.status_code == 200:
        data = json.loads(r.text)
        fact = data["fact"]
        bot.send_message(message.chat.id,
                         text=f'Now in Moscow {fact["temp"]}°, feels like {fact["feels_like"]}°. Now on the street {fact["condition"]}')
    else:
        bot.send_message(message.chat.id, 'Problems on weather API')


bot.polling(none_stop=True)

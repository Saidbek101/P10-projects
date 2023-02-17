from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '6171095511:AAFFusVwIE1guRxhYKzWtFxaQEvL2Izsy_w'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcom(message):
    result = 'Hello, How are you? '
    result += '\nWrite your sentence:'
    bot.reply_to(message, result)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     new_msg = message.text
#     if new_msg.isascii():
#         result = to_cyrillic(new_msg)
#     else:
#         result = to_latin(new_msg)
#
#     bot.reply_to(message, result)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    result = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)

    bot.reply_to(message, result(msg))


bot.polling()

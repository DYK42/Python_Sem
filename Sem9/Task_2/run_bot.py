import my_data
import  read_log
import telebot
from telebot import types
import logger


token = my_data.tele_token
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help'])
def start_bot(message):
    # print('START!')
    global bot
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Показать последние 5 операций")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="{0.first_name}! Введите арифметическое выражение".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global bot
    bot.stop_polling()


@bot.message_handler(content_types=['text'])
def func(message):
    global bot
    logger.log_by_msg(message)
    if message.text == 'Показать последние 5 операций':
        data = read_log.read_log()
        for x in range(len(data)-5, len(data)):
            bot.send_message(message.chat.id, text=f'{data[x]}')
    else:
        expression = message.text
        expression = expression.replace(' ', '')
        # print(expression)
        for x in expression:
            if x not in '+-/*%0123456789':
                bot.send_message(message.chat.id, text='Введите арифметическое выражение без букв!')
                return False
        bot.send_message(message.chat.id, text=f'{eval(expression)}')


bot.polling(none_stop=True)

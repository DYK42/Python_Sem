import my_data
import read_log
import polynom
import variables

import telebot
from telebot import types
import logger

token = "1681027383:AAE4PHlumwlOqNx2ruWx8mcmMR8CCLtTIhc"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    global bot
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # btn1 = types.KeyboardButton("Рассчитать")
    # kb.add(btn1)
    bot.send_message(message.chat.id,
                     text="{0.first_name}! Введите выражение многочлена.".format(
                         message.from_user), reply_markup=kb)


@bot.message_handler(commands=['stop'])
def stop_bot(message):
    global bot
    bot.stop_polling()


@bot.message_handler(content_types=['text'])
def func(message):
    global bot
    logger.log_by_msg(message)
    if message.text not in ['/stop', '/start', '/help']:
        variables.count += 1
        variables.lst.append(message.text)
        print(variables.lst)
        if variables.count >= 2:
            kb = types.InlineKeyboardMarkup(row_width=1)
            btn = types.InlineKeyboardButton(text='calculation', callback_data='calc')
            kb.add(btn)
            # bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, 'result = press button "calculation"', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def calculation(callback):
    if callback.data == 'calc':
        if len(variables.lst) > 1:
            pol = polynom.convert_pol(variables.lst[-1])
            pol2 = polynom.convert_pol(variables.lst[-2])
            pol_sum = polynom.sum_polynom(pol, pol2)
            s = polynom.get_polynom(pol_sum)
            kb = types.ReplyKeyboardMarkup(row_width=1)
            bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text=f'result: {s}',
                                  reply_markup=kb)


bot.polling(none_stop=True)

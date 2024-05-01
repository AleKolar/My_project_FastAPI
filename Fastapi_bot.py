from telebot import types
import PIL
from PIL import Image
import io
import pathlib
from config import telebot, bot, questions


amount = 0

questions = ['Какое время года: Зима или Лето', 'Какое время суток: День или Ночь', 'Чтоб Ты сейчас съел?']


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = "Привет!\n" \
           "Доступные команды:\n" \
           "/help - Помощь\n" \
           "/info - Информация о программе и авторе\n" \
           "/values - Увидеть список доступных валют\n" \
           "/enter - Your Choice\n" \
           "start - Your_Totem_Pet \n"
    bot.send_message(message.chat.id, text)
    # bot.register_next_step_handler(message, start)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Это может любое животное от Рыбки до Ленивца"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['info'])
def info(message: telebot.types.Message):
    text = "Your_Totem_Pet_by_AleKolar"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['enter'])
def enter(message: telebot.types.Message):
    keyboardmain = types.InlineKeyboardMarkup()
    ask_button = types.InlineKeyboardButton(text="Начнём!", callback_data="play")
    keyboardmain.add(ask_button)
    try:
        bot.send_message(message.chat.id, 'Выберите ответ', reply_markup=keyboardmain)
    except telebot.apihelper.ApiException:
        print('Error')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global amount
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('Зима', callback_data='Зима')
    btn2 = types.InlineKeyboardButton('Лето', callback_data='Лето')
    btn_0 = types.InlineKeyboardButton('Узнать результат', callback_data='Узнать результат')
    btn3 = types.InlineKeyboardButton('День', callback_data='День')
    btn4 = types.InlineKeyboardButton('Ночь', callback_data='Ночь')
    btn5 = types.InlineKeyboardButton('Сосиска в тесте', callback_data='Сосиска в тесте')
    btn6 = types.InlineKeyboardButton('Персик', callback_data='Персик')

    if call.data == "play":
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions[0],
                              reply_markup=markup)

    if call.data == 'Зима' or call.data == 'Лето':
        markup.add(btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions[1],
                              reply_markup=markup)
        if call.data == 'Зима':
            amount += 10

        else:
            if call.data == 'Лето':
                amount += 20

    if call.data == 'День' or call.data == 'Ночь':
        markup.add(btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions[1],
                              reply_markup=markup)
        if call.data == 'День':
            amount += 10
        else:
            if call.data == 'Ночь':
                amount += 30


    if call.data == 'Сосиска в тесте' or call.data == 'Персик':
        markup.add(btn_0)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=questions[2],
                              reply_markup=markup)
        if call.data == 'Сосиска в тесте':
            amount += 10
        else:
            if call.data == 'Персик':
                amount += 30


    if call.data == 'Узнать результат':
        bot.send_message(call.message.chat.id, text='Готовы!') # ТУТ ГДЕ-ТО time.sleep- НУЖЕН!
        bot.register_next_step_handler(call.message, callback_button(call))


@bot.callback_query_handler(func=lambda call: True)
def callback_button(call):
    global amount
    if amount < 40:
        p = open("img_01.jpg", 'rb')
        bot.send_photo(call.message.chat.id, p)
        #bot.send_message(message.chat.id, amount)
    elif 40 < amount < 60:
        m = open("img_02.jpg", 'rb')
        bot.send_photo(call.message.chat.id, m)
        #bot.send_message(message.chat.id, amount)
    elif 40 < amount < 90:
        m = open("img_02.jpg", 'rb')
        bot.send_photo(call.message.chat.id, m)
        #bot.send_message(message.chat.id, amount)
    else:
        m = open("img_02.jpg", 'rb')
        bot.send_photo(call.message.chat.id, m)
        #bot.send_message(message.chat.id, amount)


bot.polling(none_stop=True)

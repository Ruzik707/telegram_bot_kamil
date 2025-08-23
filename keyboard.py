import telebot
from telebot import types
from random import *
import time

# parse_mode='Markdown'
# жирным '*текст*'
# курсив '_текст_'


# старт
markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
# button_contact = types.KeyboardButton('Контакты 📱')
button_about_us = types.KeyboardButton('О НАС 🧩')
button_cheese = types.KeyboardButton('СЫРЫ 🧀')
button_price = types.KeyboardButton('Прайс-лист 🏷️')
markup_start.row(button_about_us, button_cheese, button_price)

# контакты
# markup_contact = types.InlineKeyboardMarkup()
# button_call = types.InlineKeyboardButton('Звони!', callback_data='Звони!')
# button_write = types.InlineKeyboardButton('Пиши!', url='https://t.me/diliara_salikhova')
# markup_contact.row(button_call, button_write)

# сыры
markup_cheese = types.InlineKeyboardMarkup()
button_hallumi = types.InlineKeyboardButton('Халлуми', callback_data='Халлуми')
button_cachotta = types.InlineKeyboardButton('Качотта', callback_data='Качотта')
# button_feta = types.InlineKeyboardButton('Фета', callback_data='Фета')
# button_adigeiski = types.InlineKeyboardButton('Адыгейский', callback_data='Адыгейский')
button_chechil = types.InlineKeyboardButton('Чечил', callback_data='Чечил')
button_shevr = types.InlineKeyboardButton('Шевр', callback_data='Шевр')
# button_buratta = types.InlineKeyboardButton('Буррата', callback_data='Буррата')
# button_mocarella = types.InlineKeyboardButton('Моцарелла', callback_data='Моцарелла')
button_panir = types.InlineKeyboardButton('Панир', callback_data='Панир')
button_suluguni = types.InlineKeyboardButton('Сулугуни', callback_data='Сулугуни')
# button_feta_maslo = types.InlineKeyboardButton('Фета в масле', callback_data='Фета масло')
button_shevr_maslo = types.InlineKeyboardButton('Шевр в масле', callback_data='Шевр масло')
button_montazio = types.InlineKeyboardButton('Монтазио', callback_data='Монтазио')
button_pesto = types.InlineKeyboardButton('Песто', callback_data='Песто')
button_cachocovallo = types.InlineKeyboardButton('Качоковалло', callback_data='Качоковалло')
button_canestrato = types.InlineKeyboardButton('Канестрато', callback_data='Канестрато')
button_gauda = types.InlineKeyboardButton('Гауда', callback_data='Гауда')
button_full_cheese_plate = types.InlineKeyboardButton('Полная сырная тарелка', callback_data='Полная тарелка')
button_prob_cheese_plate = types.InlineKeyboardButton('Пробная сырная тарелка', callback_data='Пробная тарелка')
markup_cheese.row(button_hallumi, button_cachotta, button_chechil, button_montazio)
markup_cheese.row(button_panir, button_suluguni, button_shevr, button_pesto, button_gauda)
markup_cheese.row(button_cachocovallo, button_canestrato, button_shevr_maslo)
markup_cheese.row(button_prob_cheese_plate,button_full_cheese_plate)

# назад к сырам
button_back_cheese = types.InlineKeyboardButton('Назад', callback_data='Назад к сырам')
button_order = types.InlineKeyboardButton('Заказать', url='https://t.me/diliara_salikhova')
markup_back_cheese = types.InlineKeyboardMarkup()
markup_back_cheese.add(button_back_cheese, button_order)
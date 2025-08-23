from text import *
from keyboard import *

token = '5689986363:AAGUuajnXodFoID7UswXLAMLASiIra4HnTE'

bot = telebot.TeleBot(token)
bot.delete_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'<i>Приветвуем вас, <b>{message.from_user.first_name}</b>, в нашем телеграмм боте!</i>',
                     reply_markup=markup_start, parse_mode='html')

@bot.message_handler(content_types=['text'])
def reply(message):
    print(f"Получено сообщение: {message.text} (ID: {message.message_id})")
    # if message.text == 'Контакты 📱':
    #     bot.send_message(message.chat.id, '<i>Звони или Пиши!</i>', reply_markup=markup_contact, parse_mode='html')
    if message.text == 'О НАС 🧩':
        bot.send_message(message.chat.id, ABOUT_US, parse_mode='html')
    elif message.text == 'СЫРЫ 🧀':
        bot.send_message(message.chat.id, '<i>Про какой <b>сыр</b> хотите узнать сегодня?</i>', reply_markup=markup_cheese, parse_mode='html')
    elif message.text == 'Прайс-лист 🏷️':
        bot.send_photo(message.chat.id, open('сыры фотки.local/all price-list.jpg', 'rb'), caption='<i>Можете ознакомиться с ценами</i>', parse_mode='html')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    print(f"Получен callback: {callback.data} (ID: {callback.id})")
    # if callback.data == 'Звони!':
    #     bot.send_contact(callback.message.chat.id, phone_number=NUMBER, first_name=NAME, last_name=SURNAME)
    if callback.data == 'Халлуми':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/халуми.jpg', 'rb'),
                       caption=hallumi, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Качотта':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/качотта.jpg', 'rb'),
                       caption=cachotta, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Фета':
    #     bot.send_photo(callback.message.chat.id, open('сыры фотки.local/фета.jpg', 'rb'),
    #                    caption=feta, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Адыгейский':
    #     bot.send_photo(callback.message.chat.id, open('сыры фотки.local/адыгейский.jpg', 'rb'),
    #                    caption=adigeiski, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Чечил':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/чечил.jpg', 'rb'),
                       caption=chechil, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Шевр':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/шевр.jpg', 'rb'),
                       caption=shevr, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Буррата':
    #     bot.send_photo(callback.message.chat.id, open('сыры фотки.local/буррата.jpg', 'rb'),
    #                    caption=buratta, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Моцарелла':
    #     bot.send_photo(callback.message.chat.id, open('сыры фотки.local/моцарелла.jpg', 'rb'),
    #                    caption=mocarella, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Полная тарелка':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/полная сырная тарелка.jpg', 'rb'),
                       caption=full_cheese_plate, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Пробная тарелка':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/пробная сырная тарелка.jpg', 'rb'),
                       caption=prob_cheese_plate, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Панир':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/панир.jpg', 'rb'),
                       caption=panir, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Сулугуни':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/сулугуни.jpg', 'rb'),
                       caption=suluguni, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Фета в масле':
    #     bot.send_photo(callback.message.chat.id, open('сыры фотки.local/.jpg', 'rb'),
    #     caption=feta_maslo, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Шевр масло':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/шевр в масле.jpg', 'rb'),
                       caption=shevr_maslo, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Монтазио':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/монтазио.jpg', 'rb'),
                       caption=montazio, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Песто':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/песто.jpg', 'rb'),
                       caption=pesto, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Качоковалло':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/качоковалло.jpg', 'rb'),
                       caption=cachocavallo, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Канестрато':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/канестрато.jpg', 'rb'),
                       caption=canestrato, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Гауда':
        bot.send_photo(callback.message.chat.id, open('сыры фотки.local/гауда.jpg', 'rb'),
                       caption=gauda, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Назад к сырам':
        bot.send_message(callback.message.chat.id, choice(back_chesse_answer), reply_markup=markup_cheese, parse_mode='html')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(1)
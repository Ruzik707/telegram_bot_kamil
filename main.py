from text import *
from keyboard import *
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if TOKEN is None:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set")

bot = telebot.TeleBot(TOKEN)
bot.delete_webhook()



def send_catalog_photo(chat_id, image_path, caption="", **kwargs):
    """Show product text when local photographs are unavailable."""
    path = Path(__file__).resolve().parent / image_path
    if not path.is_file():
        return bot.send_message(chat_id, caption or "Изображение пока недоступно.", **kwargs)
    with path.open("rb") as image:
        return bot.send_photo(chat_id, image, caption=caption, **kwargs)


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
        send_catalog_photo(message.chat.id, 'сыры фотки.local/all price-list.jpg', caption='<i>Можете ознакомиться с ценами</i>', parse_mode='html')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    print(f"Получен callback: {callback.data} (ID: {callback.id})")
    # if callback.data == 'Звони!':
    #     bot.send_contact(callback.message.chat.id, phone_number=NUMBER, first_name=NAME, last_name=SURNAME)
    if callback.data == 'Халлуми':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/халуми.jpg',
                       caption=hallumi, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Качотта':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/качотта.jpg',
                       caption=cachotta, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Фета':
    #     send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/фета.jpg',
    #                    caption=feta, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Адыгейский':
    #     send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/адыгейский.jpg',
    #                    caption=adigeiski, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Чечил':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/чечил.jpg',
                       caption=chechil, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Шевр':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/шевр.jpg',
                       caption=shevr, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Буррата':
    #     send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/буррата.jpg',
    #                    caption=buratta, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Моцарелла':
    #     send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/моцарелла.jpg',
    #                    caption=mocarella, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Полная тарелка':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/полная сырная тарелка.jpg',
                       caption=full_cheese_plate, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Пробная тарелка':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/пробная сырная тарелка.jpg',
                       caption=prob_cheese_plate, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Панир':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/панир.jpg',
                       caption=panir, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Сулугуни':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/сулугуни.jpg',
                       caption=suluguni, reply_markup=markup_back_cheese, parse_mode='html')
    # elif callback.data == 'Фета в масле':
    #     send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/.jpg',
    #     caption=feta_maslo, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Шевр масло':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/шевр в масле.jpg',
                       caption=shevr_maslo, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Монтазио':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/монтазио.jpg',
                       caption=montazio, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Песто':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/песто.jpg',
                       caption=pesto, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Качоковалло':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/качоковалло.jpg',
                       caption=cachocavallo, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Канестрато':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/канестрато.jpg',
                       caption=canestrato, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Гауда':
        send_catalog_photo(callback.message.chat.id, 'сыры фотки.local/гауда.jpg',
                       caption=gauda, reply_markup=markup_back_cheese, parse_mode='html')
    elif callback.data == 'Назад к сырам':
        bot.send_message(callback.message.chat.id, choice(back_chesse_answer), reply_markup=markup_cheese, parse_mode='html')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(1)

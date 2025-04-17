import telebot
import time
TOKEN = 'Token'
bot = telebot.TeleBot(TOKEN)
WEB_APP_URL = 'Site'

@bot.message_handler(commands=['start', 'website'])
def heartbeat():
    while True:
        try:
            bot.send_message(id_chat, "Бот роботает исправно!")
        except:
            bot.send_message(id-chat, "Бот был выключен!")
        time.sleep(1800)
def start(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(telebot.types.InlineKeyboardButton(text="Открыть сайт", web_app=web_app_button))
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы открыть сайт:", reply_markup=keyboard)

bot.polling(none_stop=True)

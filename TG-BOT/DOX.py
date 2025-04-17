import telebot
from telebot import types
import time
import sys


bot = telebot.TeleBot('Token-bot',parse_mode=None)
CHAT_ID_TO_SEND = chat-id
WEB_APP_URL = 'https://duckduckgo.com/'

@bot.message_handler(commands=['start'])
def heartbeat():
    while True:
        try:
            # Send a more informative message about bot status
            bot.send_message(-1002191507750, "Бот работает исправно! Последнее обновление информации о ключах: " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))  # Add timestamp
        except:
            # Log the error for debugging
            print("Error sending heartbeat message:", sys.exc_info()[0])
            bot.send_message(-1002191507750, "Бот был выключен! Перезапуск...")  # Inform users of outage

        time.sleep(1800)
def send_welcome(message):
    bot.reply_to(message, """При использование бота автор и разработчики софта несёт ответственность за ваши действия.
Бот Сохраняет всю историю поиска.
Для принятия что автор не несет ответственность за ваши действия на эту кнопку.
/accept """)



@bot.message_handler(commands=['accept'])
def send_welcome(message):
    bot.reply_to(message,"Нажмите /menu")



@bot.message_handler(commands=['restart', 'menu'])
def send_menu(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Поиск🔎", callback_data="button1",)
    button2 = types.InlineKeyboardButton("Софт🕵️", callback_data='button2')
    button3 = types.InlineKeyboardButton("DarkNET🏴‍☠️", callback_data='button3')
    button4 = types.InlineKeyboardButton("IP Пробив🥷", url='https://2ip.ua/ru/services/information-service/whois')
    button5 = types.InlineKeyboardButton("Мануалы📒", callback_data='button5')
    button6 = types.InlineKeyboardButton("Фейк чеки🎫",  url='https://t.me/RGT_check4bot')
    web_app_button = telebot.types.WebAppInfo(url=WEB_APP_URL)
    BRW = types.InlineKeyboardButton("Браузер 🛜", web_app=web_app_button)
    donate = types.InlineKeyboardButton("Донат💵", callback_data='donate')
    kanal = types.InlineKeyboardButton("Канал автора👉", url='https://t.me/studio_relenas')
    markup.add(button1, button2, button6)
    markup.add(button3, button4, button5)
    markup.add(BRW,donate, kanal)
    bot.send_message(message.chat.id, text="""<b>Главное меню выбор пункта:</b>
<i>Автор не несет ответственность на ваши действия</i> """,parse_mode='HTML',reply_markup=markup)

def callback_query(message):
        if message.data == "button1":
            markup = types.InlineKeyboardMarkup()
            button_2 = types.InlineKeyboardButton("Поиск", url='https://t.me/Glassboga_bot')
            button_3 = types.InlineKeyboardButton("Премиум Поиск (Недоступно.)", callback_data="info1")
            markup.add(button_2,)
            markup.add(button_3,)
            bot.send_message(message.chat.id, "Пойск", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "info1":
        bot.send_message(call.chat.id,"Поиск недоступний", parse_mode='HTML')


    if call.data == "button2":
        markup = types.InlineKeyboardMarkup()
        button_2 = types.InlineKeyboardButton("FREE SOFT", url='https://t.me/DarkSoftRelenas')
        button_3 = types.InlineKeyboardButton("PREMIUM SOFT", url='https://t.me/+RyaV1NCS4AhlM2Qy')
        markup.add(button_2,)
        markup.add(button_3,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Софт из DARKNET только для вас""",reply_markup=markup)

    if call.data == "button3":
        markup = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton("Search Engine:", callback_data="DN1")
        button_2 = types.InlineKeyboardButton("Bitcoin Anonymity:", callback_data="DN2")
        button_3 = types.InlineKeyboardButton("Stresser / Ddos", callback_data="DN3")
        button_4 = types.InlineKeyboardButton("Market:", callback_data="DN4")
        button_5 = types.InlineKeyboardButton("Database:", callback_data="DN5")
        markup.add(button_1,)
        markup.add(button_2,)
        markup.add(button_3,)
        markup.add(button_4,)
        markup.add(button_5,)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""Как зайти в Даркнет?
1.Скачайте и установите браузер Tor: Это самый популярный и безопасный способ доступа к Даркнету. Вы можете скачать 
его с официального сайта: https://www.torproject.org/ru/download/
2.Настройте Tor: После установки запустите браузер. Он автоматически настроит соединение.
3.Используйте адреса .onion: Сайты в Даркнете имеют адреса, заканчивающиеся на .onion. Их нельзя найти через обычные 
поисковики.
Будьте осторожны:
Не доверяйте всем сайтам: В Даркнете много мошенников и опасного контента.
Не скачивайте файлы с непроверенных источников: Это может привести к заражению вирусами или другими вредоносными программами.
Не раскрывайте личную информацию: Анонимность в Даркнете — это ваша главная защита.
Автор не несет ответственность на ваши действия
""",reply_markup=markup)

    if call.data == "DN1":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
[Torch]        : http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/
[Danex]        : http://danexio627wiswvlpt6ejyhpxl5gla5nt2tgvgm2apj2ofrgm44vbeyd.onion/        
[Sentor]       : http://e27slbec2ykiyo26gfuovaehuzsydffbit5nlxid53kigw3pvz6uosqd.onion/      
""",)
    if call.data == "DN2":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
[Dark Mixer]   : http://y22arit74fqnnc2pbieq3wqqvkfub6gnlegx3cl6thclos4f7ya7rvad.onion/
[Mixabit]      : http://hqfld5smkr4b4xrjcco7zotvoqhuuoehjdvoin755iytmpk4sm7cbwad.onion/
[EasyCoin]     : http://mp3fpv6xbrwka4skqliiifoizghfbjy5uyu77wwnfruwub5s4hly2oid.onion/
[Onionwallet]  : http://p2qzxkca42e3wccvqgby7jrcbzlf6g7pnkvybnau4szl5ykdydzmvbid.onion/
[VirginBitcoin]: http://ovai7wvp4yj6jl3wbzihypbq657vpape7lggrlah4pl34utwjrpetwid.onion/
""", )
    if call.data == "DN3":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
[Stresser]     : http://ecwvi3cd6h27r2kjx6ur6gdi4udrh66omvqeawp3dzqrtfwo432s7myd.onion/
        """, )
    if call.data == "DN4":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
[Deep Market]  : http://deepmar4ai3iff7akeuos3u3727lvuutm4l5takh3dmo3pziznl5ywqd.onion/
[DrChronic]    : http://iwggpyxn6qv3b2twpwtyhi2sfvgnby2albbcotcysd5f7obrlwbdbkyd.onion/
[TomAndJerry]  : http://rfyb5tlhiqtiavwhikdlvb3fumxgqwtg2naanxtiqibidqlox5vispqd.onion/
[420prime]     : http://ajlu6mrc7lwulwakojrgvvtarotvkvxqosb4psxljgobjhureve4kdqd.onion/
[Can*abisUK]   : http://7mejofwihleuugda5kfnr7tupvfbaqntjqnfxc4hwmozlcmj2cey3hqd.onion/
[DeDope]       : http://sga5n7zx6qjty7uwvkxpwstyoh73shst6mx3okouv53uks7ks47msayd.onion/
[AccMarket]    : http://55niksbd22qqaedkw36qw4cpofmbxdtbwonxam7ov2ga62zqbhgty3yd.onion/
[Cardshop]     : http://s57divisqlcjtsyutxjz2ww77vlbwpxgodtijcsrgsuts4js5hnxkhqd.onion/
[Darkmining]   : http://jbtb75gqlr57qurikzy2bxxjftzkmanynesmoxbzzcp7qf5t46u7ekqd.onion/
[MobileStore]  : http://rxmyl3izgquew65nicavsk6loyyblztng6puq42firpvbe32sefvnbad.onion/
[EuroGuns]     : http://t43fsf65omvf7grt46wlt2eo5jbj3hafyvbdb7jtr2biyre5v24pebad.onion/
[UKpassports]  : http://3bp7szl6ehbrnitmbyxzvcm3ieu7ba2kys64oecf4g2b65mcgbafzgqd.onion/
[ccPal]        : http://xykxv6fmblogxgmzjm5wt6akdhm4wewiarjzcngev4tupgjlyugmc7qd.onion/
[Webuybitcoins]: http://wk3mtlvp2ej64nuytqm3mjrm6gpulix623abum6ewp64444oreysz7qd.onion/
""", )
    if call.data == "DN5":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
[Database]     : http://breachdbsztfykg2fdaq2gnqnxfsbj5d35byz3yzj73hazydk4vq72qd.onion/
""", )

        if call.data == "button5":
            markup = types.InlineKeyboardMarkup()
            button_2 = types.InlineKeyboardButton("FREE MANUAL", url='https://t.me/FreeManualRelenas')
            button_3 = types.InlineKeyboardButton("PREMIUM MANUAL", url='https://t.me/+-AIuxL3FzU01NGNi')
            markup.add(button_2, )
            markup.add(button_3, )
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="""Мануали из DARKNET только для вас""", reply_markup=markup)


        if call.data == "donate":
            markup = types.InlineKeyboardMarkup()
            button_2 = types.InlineKeyboardButton("MONOBANK💸", url='https://send.monobank.ua/jar/4hCWns64MS')
            button_3 = types.InlineKeyboardButton("Trush Wallet", callback_data="Krypto")
            markup.add(button_2, )
            markup.add(button_3, )
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="""Допомого проекту""", reply_markup=markup)

        if call.data == "Krypto":
            markup = types.InlineKeyboardMarkup()
            KRP = types.InlineKeyboardButton("BTC", url='https://link.trustwallet.com/send?coin=0&address=bc1qe6cn8567w0j72cvj59mn9twvrl8h0r702cs7fj')
            KRP1 = types.InlineKeyboardButton("ETH", url='https://link.trustwallet.com/send?coin=60&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP2 = types.InlineKeyboardButton("TON", url='https://link.trustwallet.com/send?coin=607&address=UQB42NobC_Hz96YQOB4UqHkH8UdrCAqITqS54oqb6viubfRy')
            KRP3 = types.InlineKeyboardButton("NOT", url='https://link.trustwallet.com/send?coin=607&address=UQB42NobC_Hz96YQOB4UqHkH8UdrCAqITqS54oqb6viubfRy&token_id=EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT')
            KRP4 = types.InlineKeyboardButton("MATIС", url='https://link.trustwallet.com/send?coin=966&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP5 = types.InlineKeyboardButton("BNB", url='https://link.trustwallet.com/send?coin=20000714&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP6 = types.InlineKeyboardButton("CRO", url='https://link.trustwallet.com/send?coin=10000025&address=0x19627eaFEe2ba87c2960d080B02E5B1119A17A36')
            KRP7 = types.InlineKeyboardButton("DOGE", url='https://link.trustwallet.com/send?coin=3&address=DCapGigHcqmnHh9kvfe26cx7vJwYsRdG75')
            KRP8 = types.InlineKeyboardButton("KSM", url='https://link.trustwallet.com/send?coin=434&address=EwaCZvJHcS7evxasXiDjtruUao1R6k33kEN69GXSuMaRcj5')
            KRP9 = types.InlineKeyboardButton("TRX", url='https://link.trustwallet.com/send?coin=195&address=TLZS9HwuhD693Yp8i9MXDCDigEsKW2LVmu')
            markup.add(KRP2)
            markup.add(KRP,KRP1,KRP3)
            markup.add(KRP4,KRP5,KRP6)
            markup.add(KRP7,KRP8,KRP9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="""Мануали из DARKNET только для вас""", reply_markup=markup)




bot.polling(non_stop=True)

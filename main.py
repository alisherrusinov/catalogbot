import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
ADMINS = [
    834035462,
]
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup()
    ctlgbtn = types.InlineKeyboardButton(text='Категории')
    keyboard.add(ctlgbtn)
    bot.send_message(
        chat_id=message.chat.id,
        text='''
        Привет!\nЯ - бот, в которого можно загрузить каталог товаров с сайта, чтобы клиенты могли смотреть его прямо в телеграмме(в данной версии пока что нет оплаты, только просмотр товаров)
        ''',
        reply_markup=keyboard,
        )


@bot.message_handler(content_types=['text',])
def get_word(message):
    if(message.text.startswith('Что такое',0,9)):
        try:
            search = wikipedia.page(message.text.replace('Что такое ',''))
            answer = search.content[:300]
            keyboard = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(
                text='Ссылка на статью',
                url=search.url
            )
            keyboard.add(button)
            bot.send_message(
            chat_id=message.chat.id,
            text=answer,
            reply_markup=keyboard
        )
        except wikipedia.exceptions.DisambiguationError as error:
            bot.send_message(
                chat_id=message.chat.id,
                text=error
            )

bot.polling()
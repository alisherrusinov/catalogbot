from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from models import DBManager


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
db = DBManager()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['catalog'])
async def process_help_command(msg: types.Message):
    categories = db.get_categories()
    keyboard = types.InlineKeyboardMarkup()
    for cat in categories:
        keyboard.add(
            InlineKeyboardButton(text=cat,callback_data='azaza')
        )
    await bot.send_message(msg.from_user.id,'Категории:',reply_markup=keyboard)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
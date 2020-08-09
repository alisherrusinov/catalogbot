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
    """Получение всех категорий"""
    categories = db.get_categories()
    keyboard = types.InlineKeyboardMarkup()
    for cat in categories:
        keyboard.add(
            InlineKeyboardButton(
                text=cat,
                callback_data=f'ctg_{cat}')
        )
    await bot.send_message(msg.from_user.id,'Категории:',reply_markup=keyboard)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

@dp.callback_query_handler(lambda call: call.data and call.data.startswith('ctg_'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    """Выбирает все товары из определенной категории"""
    query = callback_query.data.replace('ctg_','')
    products = db.get_from_category(query)
    keyboard = types.InlineKeyboardMarkup()
    for product in products:
        keyboard.add(
            InlineKeyboardButton(
                text=product,
                callback_data=f'prdct_{product}'
            )
        )
    await bot.send_message(callback_query.from_user.id,f'{query}:',reply_markup=keyboard)

@dp.callback_query_handler(lambda call: call.data and call.data.startswith('prdct_'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    """Выбирает все товары из определенной категории"""
    query = callback_query.data.replace('prdct_','')
    product = db.get_product(query)
    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.a
    answer = ''
    for el in product:
        answer +=f'{el}\n'
    await bot.send_message(callback_query.from_user.id,answer)

if __name__ == '__main__':
    executor.start_polling(dp)
# Класс в котором описываются различные функции

from aiogram import types
import database
from dispatcher import dp, bot
import re


from database import botDB # Импорт базы данных и ее инициализация
botDB = botDB('db.db')


# Обрабатываем нажатие на inline-кнопку '100-тки'
@dp.callback_query_handler(text='100-тки')
async def detail_100(message: types.Message):
    botDB.add_work(message.from_user.id, str(2))
    await bot.send_message(message.from_user.id, 'Введите количество сделанных мешков')


# Обрабатываем нажатие на inline-кнопку '50-тки'
@dp.callback_query_handler(text='50-тки')
async def detail_50(message: types.Message):
    botDB.add_work(message.from_user.id, str(1))
    await bot.send_message(message.from_user.id, 'Введите количество сделанных мешков')




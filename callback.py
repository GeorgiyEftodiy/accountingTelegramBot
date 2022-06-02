# Класс в котором описываются ответы на inline-кнопкм

from aiogram import types
import database
from dispatcher import dp, bot

from database import botDB # Импорт базы данных и ее инициализация
botDB = botDB('db.db')


# Обрабатываем нажатие на inline-кнопку '⏱ История'
@dp.callback_query_handler(text='History')
async def history(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ваша личная история операций ⬇️')
    await bot.send_message(message.from_user.id, botDB.personal_prod(message.from_user.id))

@dp.callback_query_handler(text='otchet')
async def history(message: types.Message):
    pass








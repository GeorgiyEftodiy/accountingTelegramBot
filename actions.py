# Действия телеграм бота

# Импорт модулей
from aiogram import types
from dispatcher import dp, bot
import config
import re

from database import botDB
import buttons as mark


# При команде /start
@dp.message_handler(commands=['start'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Добро пожаловать {0.first_name}, чтобы зайти в свой аккаунт нажмите кнопку "Авторизация"'.format(message.from_user), reply_markup = mark.sign)

# При команде /авторизация
@dp.message_handler(commands=['Авторизация'])
async def sign_in (message: types.Message):
    users = botDB.all_users(message.from_user.id)






# Действия телеграм бота

# Импорт модулей
from aiogram import types
from dispatcher import dp, bot
import config
import re
from database import botDB
import buttons as mark
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton


@dp.message_handler(commands=['start'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Добро пожаловать {0.first_name}'.format(message.from_user), reply_markup = mark.menUser)




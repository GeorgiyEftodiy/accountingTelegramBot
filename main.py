# Основной программный код телеграм-бота

# Импортирования нужных модулей для работы с ботом
from dispatcher import dp, bot
from aiogram import executor, types
import actions
import buttons as mark

# Импорт базы данных и ее инициализация
from database import botDB
botDB = botDB('db.db')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# Основной программный код телеграм-бота

# Импортирования нужных модулей для работы с ботом
from dispatcher import dp
from aiogram import executor

import actions


from database import botDB # Импорт базы данных и ее инициализация
botDB = botDB('db.db')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

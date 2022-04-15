# Основной программный код телеграм-бота

# Импортирования нужных модулей для работы с ботом
from dispatcher import dp, bot
from aiogram import executor, types
import actions
import buttons as mark

# Импорт базы данных и ее инициализация
from database import botDB
botDB = botDB('db.db')


#                               ------ Выполнения авторизации сотрудника/админа ------
# Вход в аккаунт админа
@dp.message_handler(commands=['admin'])
async def add_work(message: types.Message):
    await bot.send_message(message.from_user.id,'Введите пароль админа')

# Авторизация сотрудника
@dp.message_handler(commands=['Авторизация👮‍♀'])
async def sign(message: types.Message):
    await bot.send_message(message.from_user.id,'Введите свой логин-пароль', reply_markup = mark.userMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

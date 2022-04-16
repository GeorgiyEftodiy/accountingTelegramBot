# Действия телеграм бота

# Импорт модулей
from aiogram import types

import database
from dispatcher import dp, bot
import config
import re

# Импорт базы данных и ее инициализация
from database import botDB
botDB = botDB('db.db')
import buttons as mark



#                ------------- Выполнения авторизации сотрудника/админа -------------
# При команде /start
@dp.message_handler(commands=['start'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Добро пожаловать {0.first_name}, '
                                                'это телеграм бот создан для сотрудников завода по производству резиновых деталей.\n'
                                                'Для начала работы с нашим ботом введите пожалуйста пароль:\n'
                                                '(Не давайте пароль постороним людям!)'.format(message.from_user), reply_markup = mark.sign)


# Вход в аккаунт админа
@dp.message_handler(commands=['admin'])
async def add_work(message: types.Message):
    await bot.send_message(message.from_user.id,'Введите пароль админа')

# Авторизация сотрудника
@dp.message_handler(commands=['Авторизация👮‍♀'])
async def sign(message: types.Message):
    await bot.send_message(message.from_user.id,'Введите свой логин-пароль', reply_markup = mark.userMenu)
# ----------------------


# При нажатии на кнопку -Записать✅-
@dp.message_handler(commands=['Записать✅'])
async def add_work(message: types.Message):
    await bot.send_message(message.from_user.id,'Вы нажимаете на кнопку - записать - и тут вы сможете записать свою работу за сегодня')

# При нажатии на кнопку -Просмотреть работу-
@dp.message_handler(commands=['Личный_кабинет👨‍🦰'])
async def cabinet(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут выводится результаты работы за текущий месяц')

# При нажатии на кнопку -Сотрудники-
@dp.message_handler(commands=['Сотрудники👥'])
async def all_users(message: types.Message):
    await message.reply(botDB.all_users())
    await bot.send_message(message.from_user.id,'Список всех сотрудников')

# При нажатии на кнопку -Итоги месяца-
@dp.message_handler(commands=['Итоги_месяца✳️'])
async def general(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут выводится общая информация всей работы за месяц')

# Руководство по пользованию ботом
@dp.message_handler(commands=['Руководство🗣'])
async def help(message: types.Message):
    await bot.send_message(message.from_user.id,'Еще раз добро пожаловать на наш телеграм-бот.\n'
                                                'После успешной авторизации вы можете пользоваться функионалом нашего бота.\n'
                                                'Здесь реализован функционал для вашего удобного учета работ на заводе. Вот ваши возможности:\n'
                                                'При нажатии на кнопку "Записать✅" вы можете записать свою работу за сегодня.\n'
                                                'При нажатии на кнопку "Просмотреть_работу💹" вы можете посмотреть свою работу за текущий месяц\n'
                                                'При нажатии на кнопку "Сотрудники👨‍🦰" вы можете просмотреть всех сотрудников завода\n'
                                                'При нажатии на кнопку "Итоги_месяца✳" вы можете увидеть общие итоги за месяц')









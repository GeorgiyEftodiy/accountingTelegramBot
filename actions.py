# Действия телеграм бота

# Импорт модулей
from aiogram import types

import database
from dispatcher import dp, bot
import config
import re
import buttons as mark

from database import botDB # Импорт базы данных и ее инициализация
botDB = botDB('db.db')

prohib = ('@','!','$')

#                ------------- Выполнения авторизации сотрудника/админа -------------
# Инициализация и регистрация пользователя
@dp.message_handler(commands = 'start')
async def start(message: types.Message):
    if (not botDB.user_exist(message.from_user.id)):
        botDB.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, 'Вы были успешно зарегистрированы в базе данных!\n'
                                                     'Пожалуйста введите ваше имя и фамилию через пробел!\n'
                                                     'Пример:Иванов Иван')
    else:
        await bot.send_message(message.from_user.id, 'Welcome')

# Авторизация сотрудника
@dp.message_handler()
async def registration(message: types.Message,):
    if message.chat.type == 'private':
        if message.text == '👮‍♀ Авторизация':
            await bot.send_message(message.from_user.id, 'Регистрация прошла успешно!', reply_markup = mark.userMenu)

        else:
            if botDB.get_signup(message.from_user.id) == 'setname':
                if '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, 'Вы ввели запрещенные символы! Пожалуйста, постарайтесь избегать их!')
                else:
                    botDB.set_name(message.from_user.id, message.text)
                    botDB.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, 'Регистрация прошла успешно!', reply_markup = mark.userMenu)


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









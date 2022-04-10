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

# При команде /Авторизация
@dp.message_handler(commands=['Авторизация👮‍♀️'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'После введения логина и пароля вы успешно заходите в аккаунт', reply_markup = mark.userMenu)

# При нажатии на кнопку -Записать✅-
@dp.message_handler(commands=['Записать✅'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Вы нажимаете на кнопку - записать - и тут вы сможете записать свою работу за сегодня')

# При нажатии на кнопку -Просмотреть работу-
@dp.message_handler(commands=['Просмотреть_работу💹'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут выводится результаты работы за текущий месяц')

# При нажатии на кнопку -Сотрудники-
@dp.message_handler(commands=['Сотрудники👨‍🦰'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут выводися список сотрудников')

# При нажатии на кнопку -Итоги месяца-
@dp.message_handler(commands=['Итоги_месяца✳️'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Тут выводится общая информация всей работы за месяц')

# При нажатии на кнопку -Руководство-
@dp.message_handler(commands=['Руководство🗣'])
async def startmenu(message: types.Message):
    await bot.send_message(message.from_user.id,'Еще раз добро пожаловать на наш телеграм-бот.  '
                                                'После успешной авторизации вы можете пользоваться функионалом нашего бота.'
                                                'При нажатии на кнопку "Записать✅" вы можете записать свою работу за сегодня.'
                                                'При нажатии на кнопку "Просмотреть_работу💹" вы можете посмотреть свою работу за текущий месяц'
                                                'При нажатии на кнопку "Сотрудники👨‍🦰" вы можете просмотреть всех сотрудников завода'
                                                'При нажатии на кнопку "Итоги_месяца✳" вы можете увидеть общие итоги за месяц')









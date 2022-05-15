# Действия телеграм бота

# Импорт модулей
from aiogram import types
import database
from dispatcher import dp, bot
import config
import re
import buttons as mark
import callback

from database import botDB # Импорт базы данных и ее инициализация
botDB = botDB('db.db')


# Инициализация и регистрация пользователя
@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    if (not botDB.user_exist(message.from_user.id)):
        botDB.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, '(Настоятельно рекомендуем прочитать руководство по пользованию ботом!)\n'
                                                     'Добро пожаловать!\n'
                                                     'Вы были успешно инициализированы в базе данных\n'
                                                     'Введите пожалуйста ваше имя и фамилию через пробел\n'
                                                     'Пример:Иванов Иван')

    else:
        if botDB.get_signup(message.from_user.id) == 'setname':
            await bot.send_message(message.from_user.id, 'Вы еще не ввели ваше имя и фамилию! Введите пожалуйста ваше имя и фамилию через пробел\n'
                                                         'Пример: Иванов Иван')
        else:
            await bot.send_message(message.from_user.id, 'Вы уже зарегистрированы! Удачной работы!',reply_markup=mark.userMenu)

# Руководство по пользованию бота
@dp.message_handler(commands=['help'])
async def general(message):
    await bot.send_message(message.from_user.id,'Руководство по пользованию:\n'
                                                'Чтобы вам открылось главное меню, вы должны успешно пройти регистрацию\n'
                                                'После регистрации внизу вы увидите ваше меню:\n'
                                                '"✅ Записать" - Нажмите данную кнопку чтобы записать вашу работу, '
                                                'после нажатия выберите какой тип деталей вы произвели и после появившегося сообщения просто '
                                                'допишите количество сделанных мешков данного типа\n'
                                                '"👨‍🦰 Личный кабинет" - Тут хранится информация о вас\n'
                                                '"👥 Сотрудники" - Список всех сотрудников(пользователей бота)')



# Обрабатывания функций
@dp.message_handler(content_types='text')
async def sign(message):
    if message.chat.type == 'private':

        # Запись ФИО для нового пользователя
        if botDB.get_signup(message.from_user.id) == 'setname':
            if '@' in message.text or '/' in  message.text:
                await bot.send_message(message.from_user.id, 'Вы ввели запрещенный символ!')
            else:
                botDB.set_name(message.from_user.id, message.text)
                botDB.set_signup(message.from_user.id, "succes")
                await bot.send_message(message.from_user.id, 'Регистрация прошла успешно! Удачной работы!', reply_markup=mark.userMenu)


        # Работа основного меню сотрудника
        if message.text == '👨‍🦰 Личный кабинет':
            await bot.send_message(message.from_user.id, '👨‍🦰 Ваш аккаунт: ' + botDB.get_name(message.from_user.id) + '\n'
                                                         '✳️ Ваш телеграм ID: ' + str(message.from_user.id) + '\n'
                                                         '✔️ Сделанных мешков: \n'
                                                         '✔️ Заработано денег: ')
        if message.text == '👥 Сотрудники':
            await bot.send_message(message.from_user.id, 'Список сотрудников ⬇️')
            await bot.send_message(message.from_user.id, botDB.all_users())

        if message.text == '🛠 Производство':
            await bot.send_message(message.from_user.id, 'Список сотрудников ⬇️')
            await bot.send_message(message.from_user.id, botDB.all_prod())


             # ---------------- Запись работ сотрудников ----------------
        if message.text == '✅ Записать':
            await bot.send_message(message.from_user.id, 'Сейчас мы запишем вашу работу!\n'
                                                         'Выберите тип деталей который вы произвели  ⬇\n'
                                                         '(После выбора просто допишите количество сделанных мешков)', reply_markup=mark.inline_detali)
        if '@zavodrezbot Тип(100) Количество=' in message.text:
            amount = message.text[33:]
            botDB.add_work(message.from_user.id, '100', amount)
            await bot.send_message(message.from_user.id, '✔️ Вы успешно добавили ' + amount + ' мешков типа 100-тки\n'
                                                         "Ваши общие результаты вы можете посмотреть в '👨‍🦰 Личный кабинет'")

        if '@zavodrezbot Тип(50) Количество=' in message.text:
            amount = message.text[32:]
            botDB.add_work(message.from_user.id, '50', amount)
            await bot.send_message(message.from_user.id, '✔️ Вы успешно добавили ' + amount + ' мешков типа 50-тки\n'
                                                         "Ваши общие результаты вы можете посмотреть в '👨‍🦰 Личный кабинет'")
            # --------------------------------------------------------------















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









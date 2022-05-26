# Действия телеграм бота

# Импорт модулей
from aiogram import types
from dispatcher import dp, bot

import buttons as mark
import callback

import datetime

import database
from database import botDB # Импорт базы данных и ее инициализация
botDB = botDB('db.db')

# Список пользователей которые имеют права админа
adminlist = ['1463808811']

# Регистрация пользователя
@dp.message_handler(commands = ['start'])
async def start(message: types.Message):

    if (botDB.user_exist(message.from_user.id)):
        await bot.send_message(message.from_user.id, 'Добро пожаловать!\n'
                                                     'Вы были найдены в базе данных, значит вы являетесь сотрудником нашего предприятия!\n'
                                                     'Ваше имя ({1} - {0}) тоже записано в базе данных.\n'
                                                     '🎉 Удачного пользованья 🎉'.format(message.from_user.first_name, message.from_user.last_name ), reply_markup=mark.userMenu)

        if (botDB.get_name(message.from_user.id)) == 'setname':
            name = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name)
            botDB.set_name(message.from_user.id, name)

    else:
        await bot.send_message(message.from_user.id, 'Извините, но вы не можете пользоваться нашим ботом т.к вы не являетесь сотрудником предприятия на данный момент 😔\n'
                                                     'Обратитесь к нашему администратору @georgyeftody пожалуйста. Ваш ID:' + str(message.from_user.id))

# Руководство по пользованию бота
@dp.message_handler(commands=['help'])
async def general(message):
    await bot.send_message(message.from_user.id,'📍 Руководство по пользованию:\n'
                                                '📍 Чтобы вы могли пользоваться ботом, необходимо чтобы админ добавил вас в базу данных❗\n'
                                                '📍 Если вы есть в базе данных то вам откроется меню пользователя.\n\n'
                                                '🔹 Вот какие функции вам будут доступны ⬇️\n\n'
                                                '🔹 ✅ Записать - Нажмите данную кнопку чтобы записать вашу работу, '
                                                'после нажатия выберите какой тип деталей вы произвели и после появившегося сообщения просто '
                                                'допишите количество сделанных мешков данного типа и отправте сообщения боту.\n\n'
                                                '🔹 👨‍🦰 Личный кабинет - Тут хранится информация о вас и вашей работы\n\n'
                                                '🔹 👥 Сотрудники - Список всех сотрудников(пользователей бота)\n\n'
                                                '🔹 🛠 Производство - История всех работ на предприятии\n\n'
                                                '🔹 ❌ Удалить запись работы - Если вы неправильно записали вашу работу, вы можете удалить неверную запись.'
                                                'Нажмите на данную кнопку, после чего нажмите на нижнюю кнопку которая появится(❌Удалить запись) '
                                                'и в конце сообщения которое появится, допишите номер записи работы которую нужно удалить и отправте сообщение боту '
                                                '(Чтобы узнать номер записи работы которая вам нужна нажмите на кнопку "⏱ История")')

# Добавления сотрудника
@dp.message_handler(commands=['adduser'])
async def adduser(message):
    if str(message.from_user.id) in adminlist:
        await bot.send_message(message.from_user.id,'👨‍🦱 Добавления нового пользователя:', reply_markup=mark.inline_adduser)
    else:
        await bot.send_message(message.from_user.id, 'У вас нет прав для использования данной команды ❗️❗️❗️')


# Удаления сотрудника
@dp.message_handler(commands=['deleteuser'])
async def deleteuser(message):
    if str(message.from_user.id) in adminlist:
        await bot.send_message(message.from_user.id,'👨‍🦱 Удаления сотрудника из БД:', reply_markup=mark.inline_deleteuser)
    else:
        await bot.send_message(message.from_user.id, 'У вас нет прав для использования данной команды ❗️❗️❗️')


# Редактирование стоимости деталей
@dp.message_handler(commands=['editdetail'])
async def editdetail(message):
    if str(message.from_user.id) in adminlist:
        await bot.send_message(message.from_user.id,'Выберите, стоимость какого типа деталей нужно изменить? ⬇', reply_markup=mark.edit_detail)
    else:
        await bot.send_message(message.from_user.id, 'У вас нет прав для использования данной команды ❗️❗️❗️')


# Обработка сообщений
@dp.message_handler(content_types='text')
async def sign(message):

    # Команды администратора
    if str(message.from_user.id) in adminlist:
        if '@zavodrezbot Введите TelegramID пользователя:' in message.text:
            userid = message.text[45:]
            botDB.add_user(userid)
            await bot.send_message(message.from_user.id,'☑️ Вы успешно добавили сотрудника с ID=' + str(userid))

        if '@zavodrezbot Введите новую стоимость детали(50-тки):' in message.text:
            newCost = message.text[52:]
            botDB.new_cost(newCost, 1)
            await bot.send_message(message.from_user.id, '☑️ Вы успешно обновили стоимость детали(50-тки)')

        if '@zavodrezbot Введите новую стоимость детали(100-тки):' in message.text:
            newCost = message.text[53:]
            botDB.new_cost(newCost, 2)
            await bot.send_message(message.from_user.id, '☑️ Вы успешно обновили стоимость детали(100-тки)')

        if '@zavodrezbot Введите ID сотрудника:' in message.text:
            userid = message.text[35:]
            botDB.delete_user(userid)
            await bot.send_message(message.from_user.id, '☑️ Вы успешно удалили пользователя с номером: ' + str(userid))



    # Если пользователь добавлен в БД то имеет доступ к след функциям
    if (botDB.user_exist(message.from_user.id)):
        if message.chat.type == 'private':

            # Работа основного меню сотрудника ⬇

            # Личный кабинет
            if message.text == '👨‍🦰 Личный кабинет':
                await bot.send_message(message.from_user.id, '⏳ Дата: ' + str(datetime.datetime.today().strftime("%d-%m-%Y")) + '\n\n'
                                                             '👨‍🦰 Ваш аккаунт: ' + botDB.get_name(message.from_user.id) + '\n'
                                                             '📲 Ваш TelegramID: ' + str(message.from_user.id) + '\n\n'
                                                             '✔️ Сделанных мешков: \n'
                                                             '✔️ Заработано денег: ', reply_markup=mark.inline_personalArea)

            # Вывод информации о сотрудниках
            if message.text == '👥 Сотрудники':
                await bot.send_message(message.from_user.id, 'Список сотрудников ⬇️')
                await bot.send_message(message.from_user.id, botDB.all_users())

            # Информация о производстве
            if message.text == '🛠 Производство':
                await bot.send_message(message.from_user.id, 'Сегодняшняя дата: ' + str(datetime.datetime.today().strftime("%d-%m-%Y")) + '\n'
                                                             'Работа на заводе ⬇️')
                await bot.send_message(message.from_user.id, botDB.all_prod())


             # ---------------- Запись работ сотрудников ----------------
            if message.text == '✅ Записать':
                await bot.send_message(message.from_user.id, 'Сейчас мы запишем вашу работу!\n'
                                                             'Выберите тип деталей который вы произвели  ⬇\n'
                                                             '(После выбора просто допишите количество сделанных мешков)', reply_markup=mark.inline_detali)

            if '@zavodrezbot Тип(100) Количество=' in message.text:
                amount = message.text[33:]
                summ = int(amount) * int(botDB.get_cost_detail(2))
                botDB.add_work(message.from_user.id, message.from_user.first_name, '100', amount, summ)
                await bot.send_message(message.from_user.id, '✔️ Вы успешно добавили ' + str(amount) + ' мешков типа 100-тки\n'
                                                             "Ваши общие результаты вы можете посмотреть в '👨‍🦰 Личный кабинет'")

            if '@zavodrezbot Тип(50) Количество=' in message.text:
                amount = message.text[32:]
                summ = int(amount) * int(botDB.get_cost_detail(1))
                botDB.add_work(message.from_user.id, message.from_user.first_name, '50', amount, summ)
                await bot.send_message(message.from_user.id, '✔️ Вы успешно добавили ' + str(amount) + ' мешков типа 50-тки\n'
                                                         "Ваши общие результаты вы можете посмотреть в '👨‍🦰 Личный кабинет'")
                # --------------------------------------------------------------


            # Удаления записи о работе сотрудника
            if message.text == '❌ Удалить запись работы':
                await bot.send_message(message.from_user.id, 'Чтобы удалить неверную запись о вашей работе нажмите на кнопку "Удалить запись" ⬇️\n'
                                                             '(После нажатия вам нужно будет дописать номер операции которая должна быть удалена! '
                                                             'Если вы не знаете номер то нажмите на кнопку "История" и найдите нужный вам номер)', reply_markup=mark.inline_deleteprod)

            if '@zavodrezbot Введите номер неверной записи:' in message.text:
                botDB.delete_work(message.text[43:])
                await bot.send_message(message.from_user.id, '✔️ Вы успешно удалили запись с номером: ' + str(message.text[43:]))


    else:
        await bot.send_message(message.from_user.id,'Извините, но вы не можете пользоваться нашим ботом т.к вы не являетесь сотрудником предприятия на данный момент 😔\n'
                                                    'Обратитесь к нашему администратору @georgyeftody пожалуйста. Ваш ID:' + str(message.from_user.id))















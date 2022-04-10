# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton

# ------ Авторизация ------
signbtn = KeyboardButton('/Авторизация👮‍♀️')
sign = ReplyKeyboardMarkup(resize_keyboard=True).add(signbtn)

# ------ Меню сторудников ------
zapisBtn = KeyboardButton('/Записать✅')
prosmotrlBtn = KeyboardButton('/Просмотреть_работу💹')
userslBtn = KeyboardButton('/Сотрудники👨‍🦰')
itogBtn = KeyboardButton('/Итоги_месяца✳️')
rucovodstvoBtn = KeyboardButton('/Руководство🗣')
userMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(zapisBtn, prosmotrlBtn, userslBtn, itogBtn, rucovodstvoBtn)
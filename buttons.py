# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton

# ------ Авторизация ------
signbtn = KeyboardButton('/Авторизация👮‍♀️')
sign = ReplyKeyboardMarkup(resize_keyboard=True).add(signbtn)

# ------ Меню сторудников ------
zapisBtn = KeyboardButton('/Записать✅')
prosmotrlBtn = KeyboardButton('/Личный_кабинет💹')
usersBtn = KeyboardButton('/Сотрудники👨‍🦰')
rucovodstvoBtn = KeyboardButton('/Руководство🗣')
userMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(zapisBtn, prosmotrlBtn, usersBtn, rucovodstvoBtn)

# ------ Меню Администратора ------
usersBtn = KeyboardButton('/Сотрудники✅')
detaliBtn = KeyboardButton('/Детали💹')
workBtn = KeyboardButton('/Производство👨‍🦰')
itogBtn = KeyboardButton('/Итоги_месяца✳️')
adminInstrBtn = KeyboardButton('/Руководство🗣')
adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(usersBtn, detaliBtn, workBtn,itogBtn, adminInstrBtn )
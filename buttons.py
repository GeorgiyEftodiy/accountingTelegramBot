# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# keyboards.py
inline_btn_1 = InlineKeyboardButton(text='50-тки', callback_data='50-тки')
inline_btn_2 = InlineKeyboardButton(text='100-тки', callback_data='100-тки')
inline_detali = InlineKeyboardMarkup(row_width=2).add(inline_btn_1, inline_btn_2)

# ------ Меню сторудников ------
zapisBtn = KeyboardButton('✅ Записать')
prosmotrlBtn = KeyboardButton('👨‍🦰 Личный кабинет')
usersBtn = KeyboardButton('👥 Сотрудники')
userMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(zapisBtn, prosmotrlBtn, usersBtn)

# ------ Тип деталей------
fifty = KeyboardButton('50-тки')
onehundred = KeyboardButton('100-тки')
backmenu = KeyboardButton('🔙 Меню')
detali = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(fifty, onehundred, backmenu)

# ------ Меню Администратора ------
usersBtn = KeyboardButton('/Сотрудники✅')
detaliBtn = KeyboardButton('/Детали💹')
workBtn = KeyboardButton('/Производство👨‍🦰')
itogBtn = KeyboardButton('/Итоги_месяца✳️')
adminInstrBtn = KeyboardButton('/Руководство🗣')
adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(usersBtn, detaliBtn, workBtn,itogBtn, adminInstrBtn )
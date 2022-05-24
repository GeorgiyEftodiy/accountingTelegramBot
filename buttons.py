# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# Инлайн кнопки - тип деталей
inline_btn_50 = InlineKeyboardButton(text='50-тки', switch_inline_query_current_chat ='Тип(50) Количество=')
inline_btn_100 = InlineKeyboardButton(text='100-тки', switch_inline_query_current_chat ='Тип(100) Количество=')
inline_detali = InlineKeyboardMarkup(row_width=2).add(inline_btn_100, inline_btn_50)

# ------ Меню сторудников ------
zapisBtn = KeyboardButton('✅ Записать')
personal = KeyboardButton('👨‍🦰 Личный кабинет')
usersBtn = KeyboardButton('👥 Сотрудники')
work = KeyboardButton('🛠 Производство')
userMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(zapisBtn, personal, usersBtn, work)



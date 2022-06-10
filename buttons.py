# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup



# Инлайн кнпки для личного кабинета
inline_btn_history = InlineKeyboardButton(text='⏱ История работы', callback_data='History')
inline_personalArea = InlineKeyboardMarkup(row_width=1).add(inline_btn_history)


# Инлайн кнопки - Удаления неверной записи
inline_btn_history = InlineKeyboardButton(text='⏱ История', callback_data='History')
inline_btn_deleteP = InlineKeyboardButton(text='❌ Удалить запись', switch_inline_query_current_chat ='Введите номер неверной записи:')
inline_deleteprod = InlineKeyboardMarkup(row_width=2).add(inline_btn_deleteP, inline_btn_history)


# Инлайн кнопка - Добавить пользователя
inline_btn_adduser = InlineKeyboardButton(text='Добавить сотрудника', switch_inline_query_current_chat ='Введите TelegramID пользователя:')
inline_adduser = InlineKeyboardMarkup(row_width=2).add(inline_btn_adduser)


# Инлайн кнопка - Удалить пользователя
inline_btn_deleteuser = InlineKeyboardButton(text='Удалить сотрудника', switch_inline_query_current_chat ='Введите ID сотрудника:')
inline_deleteuser = InlineKeyboardMarkup(row_width=2).add(inline_btn_deleteuser)


# Инлайн кнопки для редакирования стоимости детали
inline_edit_50 = InlineKeyboardButton(text='Тип:50-тки', switch_inline_query_current_chat ='Введите новую стоимость детали(50-тки):')
inline_edit_100 = InlineKeyboardButton(text='Тип:100-тки', switch_inline_query_current_chat ='Введите новую стоимость детали(100-тки):')
edit_detail = InlineKeyboardMarkup(row_width=2).add(inline_edit_50, inline_edit_100)


# Инлайн кнопки - тип деталей
inline_btn_50 = InlineKeyboardButton(text='50-тки', switch_inline_query_current_chat ='Тип(50) Количество=')
inline_btn_100 = InlineKeyboardButton(text='100-тки', switch_inline_query_current_chat ='Тип(100) Количество=')
inline_detali = InlineKeyboardMarkup(row_width=2).add(inline_btn_100, inline_btn_50)


# ------ Меню сторудников ------
zapisBtn = KeyboardButton('✅ Записать')
personal = KeyboardButton('👨‍🦰 Личный кабинет')
usersBtn = KeyboardButton('👥 Сотрудники')
work = KeyboardButton('🛠 Производство')
deletework = KeyboardButton('❌ Удалить запись работы')
otchet = KeyboardButton('📈 Создать отчет')
userMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(zapisBtn, personal, usersBtn, work, deletework, otchet)



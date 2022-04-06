# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton

# ------ Авторизация ------
signbtn = KeyboardButton('Авторизация 👮‍♀️')
sign = ReplyKeyboardMarkup(resize_keyboard=True).add(signbtn)
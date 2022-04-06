# Файл для создание кнопок

# Импорт нужных модулей
from aiogram.types import ReplyKeyboardMarkup,\
                         KeyboardButton

# ------ Menu users ------

button1 = KeyboardButton('Текущий месяц 💹')
button2 = KeyboardButton('Записать ✅')
button3 = KeyboardButton('Все сотрудники 👦')
button4 = KeyboardButton('Итоги месяца ⌛')
button5 = KeyboardButton('Руководство 🚑')
menUser = ReplyKeyboardMarkup(resize_keyboard=True).add(button1,button2,button3,button4,button5)
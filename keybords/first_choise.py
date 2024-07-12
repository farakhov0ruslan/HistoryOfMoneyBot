from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1=KeyboardButton("Информация")
button2=KeyboardButton("Конвертация")



kb_first_choise=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_first_choise.row(button1, button2)
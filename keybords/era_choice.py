from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton("Денежные единицы древней Руси XI - XV вв")
button2 = KeyboardButton("Денежные единицы Московии XVI-XVII вв.")
button3 = KeyboardButton("Денежные единицы России XVIII-XIX вв.")
button4 = KeyboardButton("Денежные единицы России с 1897 г по 1914 г.")
button5 = KeyboardButton("Денежные единицы СССР")

era_kb=ReplyKeyboardMarkup(resize_keyboard=True)
era_kb.row(button1).row(button2).row(button3).row(button4).row(button5)

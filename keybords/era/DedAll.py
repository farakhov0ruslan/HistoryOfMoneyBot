from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Древняя русь
Dr_Ru_button1 = KeyboardButton("Гривна серебра")
Dr_Ru_button2 = KeyboardButton("Гривна кун (1/4 Гривны серебра)")
Dr_Ru_button3 = KeyboardButton("Ногата (1/20 Гривны кун)")
Dr_Ru_button4 = KeyboardButton("Куна")
Dr_Ru_button5 = KeyboardButton("Резана")

Dr_Ru_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
Dr_Ru_kb.row(Dr_Ru_button1, Dr_Ru_button2).row(Dr_Ru_button3, Dr_Ru_button4).row(Dr_Ru_button5)

# Денежные единицы Московии XVI-XVII вв.
Mosk_button1 = KeyboardButton("Рубль счетный (1/3 Гривны серебра)")
Mosk_button2 = KeyboardButton("Алтын")
Mosk_button3 = KeyboardButton("Копейка (Новгородка)")
Mosk_button4 = KeyboardButton("Деньга (Московка)")
Mosk_button5 = KeyboardButton("Полушка")

Mosk_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
Mosk_kb.row(Mosk_button1, Mosk_button2).row(Mosk_button3, Mosk_button4).row(Mosk_button5)

# Денежные единицы России XVIII-XIX вв.
RusXVIII_button1 = KeyboardButton("Империал (10 рублей серебром)")
RusXVIII_button2 = KeyboardButton("Рубль серебром")
RusXVIII_button3 = KeyboardButton("Рубль ассигнациями до 1840 г.")
RusXVIII_button4 = KeyboardButton("Рубль ассигнациями с 1840 г.")
RusXVIII_button5 = KeyboardButton("Копейка серебром")
RusXVIII_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
RusXVIII_kb.row(RusXVIII_button1).row(RusXVIII_button2)\
    .row(RusXVIII_button3).row(RusXVIII_button4).row(RusXVIII_button5)

# Денежные единицы России с 1897 г по 1914 г.
Rus1897_1914_button1 = KeyboardButton("Империал (15 рублей серебром)")
Rus1897_1914_button2 = KeyboardButton("Рубль")
Rus1897_1914_button3 = KeyboardButton("Копейка")
Rus1897_1914_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
Rus1897_1914_kb.row(Rus1897_1914_button1).row(Rus1897_1914_button2).row(Rus1897_1914_button3)

# Денежные единицы СССР
USSR_button1 = KeyboardButton("Рубль на 1937")
USSR_button2 = KeyboardButton("Рубль на 1947")
USSR_button3 = KeyboardButton("Рубль на 1980")
USSR_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
USSR_kb.row(USSR_button1).row(USSR_button2).row(USSR_button3)

kb_all = {
    "Денежные единицы древней Руси XI - XV вв": Dr_Ru_kb,
    "Денежные единицы Московии XVI-XVII вв.": Mosk_kb,
    "Денежные единицы России XVIII-XIX вв.":RusXVIII_kb,
    "Денежные единицы России с 1897 г по 1914 г.": Rus1897_1914_kb,
    "Денежные единицы СССР":USSR_kb
}

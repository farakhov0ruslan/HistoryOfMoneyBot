from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btn1=KeyboardButton("Денежное обращение в период Древней Руси")
btn2=KeyboardButton("Безмонетный период на Руси в 12-14 вв.")
btn3=KeyboardButton("Монеты периода объединения Русского государства")
btn4=KeyboardButton("Денежная система России и её развитие в XVI-XVII вв.")
btn5=KeyboardButton("Развитие денежной системы в Российской Империи")
btn6=KeyboardButton("Развитие денежной системы в СССР")
btn7=KeyboardButton("Монеты и банкноты РФ")
btn_back=KeyboardButton("Назад")

info_money_kb=ReplyKeyboardMarkup(resize_keyboard=True).\
    row(btn1).row(btn2).row(btn3).row(btn4).add(btn5).add(btn6).add(btn7).add(btn_back)
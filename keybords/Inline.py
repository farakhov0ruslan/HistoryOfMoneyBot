from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='/Dr_Ru_button1')
inline_btn_2 = InlineKeyboardButton('Вторая кнопка!', callback_data='/button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)

from .info_handler import InfoHandler
from .converter import Converter
from .converter import FSM_client
import keybords.Inline
from aiogram import types, Dispatcher
from keybords import first_choise, info_money
from keybords.first_choise import kb_first_choise
from emoji import emojize


async def open_info_money(message: types.Message):
    await message.answer("Выбери нужный промежуток времени",
                         reply_markup=keybords.info_money.info_money_kb)


async def command_back(message: types.Message):
    await message.answer(text="Первоначальное меню", reply_markup=kb_first_choise)


def cmd(message: types.Message, command: str):
    string = message.text
    if string == command or string == "/" + command:
        return string


async def commands_start(message=types.Message):
    await message.answer(
        "Привет" + emojize(":waving_hand:") + "! Я бот который можете тебе рассказать о " + emojize(
            ":coin:") + ""
                        " деньгах или конвертировать денежные"
                        " единицы прошлого в нынешний курс ₽."
                        " Для всего этого следуй инструкциям",
        reply_markup=keybords.first_choise.kb_first_choise)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, lambda x: cmd(x, "start"))
    dp.register_message_handler(open_info_money, lambda x: cmd(x, "Информация"))
    dp.register_message_handler(InfoHandler.answer_info_money,
                                lambda x: InfoHandler.determinate_era(x))
    dp.register_message_handler(command_back, lambda x: cmd(x, "Назад"))
    dp.register_message_handler(Converter.cmd_start_converter,
                                lambda x: cmd(x, "Конвертация"), state=None)
    dp.register_message_handler(Converter.converter_era, state=FSM_client.era)
    dp.register_message_handler(Converter.converter_currency, state=FSM_client.currency)
    dp.register_message_handler(Converter.converter_count, state=FSM_client.count)

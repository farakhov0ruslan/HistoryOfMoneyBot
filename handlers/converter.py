from aiogram import types

from keybords import first_choise, era_choice
from keybords.era.DedAll import kb_all
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_client(StatesGroup):
    era = State()
    currency = State()
    count = State()


class Converter:
    coefficient = {
        "Денежные единицы древней Руси XI - XV вв": {
            "Гривна серебра": 14280,
            "Гривна кун (1/4 Гривны серебра)": 3570,
            "Ногата (1/20 Гривны кун)": 178.5,
            "Куна": 142.8,
            "Резана": 71.4},

        "Денежные единицы Московии XVI-XVII вв.": {
            "Рубль счетный (1/3 Гривны серебра)": 4760,
            "Алтын": 142.8,
            "Копейка (Новгородка)": 47.6,
            "Деньга (Московка)": 23.8,
            "Полушка": 11.9},

        "Денежные единицы России XVIII-XIX вв.": {
            "Империал (10 рублей серебром)": 12596.5000,
            "Рубль серебром": 1259.65,
            "Рубль ассигнациями до 1840 г.": 999.7222,
            "Рубль ассигнациями с 1840 г.": 359.9000,
            "Копейка серебром": 12.5965},

        "Денежные единицы России с 1897 г по 1914 г.": {
            "Империал (15 рублей серебром)": 24400.9500,
            "Рубль": 1626.73,
            "Копейка": 16.2673, },

        "Денежные единицы СССР": {
            "Рубль на 1937": 1010.570,
            "Рубль на 1947": 1353.48,
            "Рубль на 1980": 197
        }
    }

    @staticmethod
    async def cmd_start_converter(message: types.Message):
        await FSM_client.era.set()
        await message.answer("Выберите промежуток времени", reply_markup=era_choice.era_kb)

    @staticmethod
    async def converter_era(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["era"] = message.text
        await FSM_client.next()
        try:
            await message.reply("Выберите валюту", reply_markup=kb_all[message.text])
        except KeyError:
            await message.answer("Неверное введенны данные, попробуйте ещё раз",
                                 reply_markup=first_choise.kb_first_choise)
            await state.finish()

    @staticmethod
    async def converter_currency(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["currency"] = message.text
        await FSM_client.next()
        await message.answer(f"Введите количество денежных единиц({message.text})"
                             f" для перевод в современную валюту ₽")

    @staticmethod
    async def converter_count(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data["count"] = message.text
        async with state.proxy() as data:
            try:
                cnt = int(message.text)
                era = data["era"]
                currency = data["currency"]
                now_curs = round(cnt * Converter.coefficient[era][currency], 4)
                await message.answer(f"{cnt} ({currency}) = {now_curs}₽",
                                     reply_markup=first_choise.kb_first_choise)
            except:
                await state.finish()
                await message.answer("Вы неправильно ввели данные, повторите попытку",
                                     reply_markup=first_choise.kb_first_choise)

        await state.finish()

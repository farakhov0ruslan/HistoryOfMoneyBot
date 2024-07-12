from aiogram import types, Dispatcher
from sqlalchemy import select
from sqlalchemy.orm import selectinload

import keybords.Inline
from database.engine import get_session
from database.models import EraInfo
from keybords import first_choise, info_money, era_choice
from keybords.era.DedAll import kb_all
from create_bot import bot
from keybords.first_choise import kb_first_choise
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from converter import coefficient
from aiogram.types import InputFile
from emoji import emojize


async def answer_info_money(message: types.Message):
    async with get_session() as session:
        try:
            existing_era = await session.execute(
                select(EraInfo).options(selectinload(EraInfo.items)).where(
                    EraInfo.name == message.text)
            )
            era = existing_era.scalar_one_or_none()

            if era and era.items:
                # Используем данные из базы для ответа
                for item in era.items:
                    if item.type == "text":
                        await message.answer(item.content, parse_mode="Markdown")
                    elif item.type == "image":
                        await bot.send_photo(chat_id=message.chat.id, photo=InputFile(item.content))
            else:
                await message.answer("Информация не найдена или повреждена.")
        except Exception as e:
            await session.rollback()
            print(f"An error occurred: {e}")
            await message.answer("Произошла ошибка при обработке запроса.")


def determinate_era(message: types.Message):
    era = ["Денежное обращение в период Древней Руси",
           "Безмонетный период на Руси в 12-14 вв.",
           "Монеты периода объединения Русского государства",
           "Денежная система России и её развитие в XVI-XVII вв.",
           "Развитие денежной системы в Российской Империи",
           "Развитие денежной системы в СССР",
           "Монеты и банкноты РФ"]
    txt = message.text
    if txt.replace("/", "") in era:
        return [txt]


def cmd(message: types.Message, command: str):
    string = message.text
    if string == command or string == "/" + command:
        return string


def deng_ed(message: types.Message):
    mes_deng_ed = message.text
    print("Денежные единицы" in mes_deng_ed, mes_deng_ed)
    if "Денежные единицы" in mes_deng_ed:
        return message


class FSM_client(StatesGroup):
    era = State()
    currency = State()
    count = State()


async def cmd_start_converter(message: types.Message):
    await FSM_client.era.set()
    await message.answer("Выберите промежуток времени", reply_markup=era_choice.era_kb)


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


async def converter_currency(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["currency"] = message.text
    await FSM_client.next()
    await message.answer(f"Введите количество денежных единиц({message.text})"
                         f" для перевод в современную валюту ₽")


async def converter_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["count"] = message.text
    async with state.proxy() as data:
        try:
            cnt = int(message.text)
            era = data["era"]
            currency = data["currency"]
            now_curs = round(cnt * coefficient[era][currency], 4)
            await message.answer(f"{cnt} ({currency}) = {now_curs}₽",
                                 reply_markup=first_choise.kb_first_choise)
        except:
            await state.finish()
            await message.answer("Вы неправильно ввели данные, повторите попытку",
                                 reply_markup=first_choise.kb_first_choise)

    await state.finish()


async def commands_start(message=types.Message):
    await message.answer(
        "Привет" + emojize(":waving_hand:") + "! Я бот который можете тебе рассказать о " + emojize(
            ":coin:") + ""
                        " деньгах или конвертировать денежные"
                        " единицы прошлого в нынешний курс ₽."
                        " Для всего этого следуй инструкциям",
        reply_markup=keybords.first_choise.kb_first_choise)


async def open_info_money(message: types.Message):
    await message.answer("Выбери нужный промежуток времени",
                         reply_markup=keybords.info_money.info_money_kb)


async def command_back(message: types.Message):
    await message.answer(text="Первоначальное меню", reply_markup=kb_first_choise)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, lambda x: cmd(x, "start"))
    dp.register_message_handler(open_info_money, lambda x: cmd(x, "Информация"))
    dp.register_message_handler(answer_info_money, lambda x: determinate_era(x))
    dp.register_message_handler(command_back, lambda x: cmd(x, "Назад"))
    dp.register_message_handler(cmd_start_converter, lambda x: cmd(x, "Конвертация"), state=None)
    dp.register_message_handler(converter_era, state=FSM_client.era)
    dp.register_message_handler(converter_currency, state=FSM_client.currency)
    dp.register_message_handler(converter_count, state=FSM_client.count)

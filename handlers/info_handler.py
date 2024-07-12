from aiogram import types
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from database.engine import get_session
from database.models import EraInfo
from create_bot import bot
from aiogram.types import InputFile


class InfoHandler:
    @staticmethod
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
                            await bot.send_photo(chat_id=message.chat.id,
                                                 photo=InputFile(item.content))
                else:
                    await message.answer("Информация не найдена или повреждена.")
            except Exception as e:
                await session.rollback()
                print(f"An error occurred: {e}")
                await message.answer("Произошла ошибка при обработке запроса.")

    @staticmethod
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

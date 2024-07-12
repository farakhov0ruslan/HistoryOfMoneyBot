from aiogram.utils import executor
from create_bot import dp
from database.engine import create_db
from handlers import app

app.register_handlers_client(dp)


async def on_startup(_):
    print("Bot online!")
    await create_db()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

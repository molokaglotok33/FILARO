import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.menu import router as menu_router
from handlers.start import router as start_router


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")


bot = Bot(token=TOKEN)

dp = Dispatcher()

# Подключаем обработчики
dp.include_router(start_router)
dp.include_router(menu_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from keyboards.main_menu import main_menu
from handlers.menu import router as menu_router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(menu_router)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🚀 Добро пожаловать в FILARO!\n\n"
        "Выберите действие 👇",
        reply_markup=main_menu,
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
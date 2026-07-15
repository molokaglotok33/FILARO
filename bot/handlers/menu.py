from aiogram import F, Router
from aiogram.types import CallbackQuery

from keyboards.main_menu import main_menu
from keyboards.plans import plans_keyboard

router = Router()


@router.callback_query(F.data == "buy")
async def buy_subscription(callback: CallbackQuery):
    await callback.message.edit_text(
        "💎 Выберите тариф",
        reply_markup=plans_keyboard,
    )

    await callback.answer()


@router.callback_query(F.data == "back_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "🚀 Добро пожаловать в FILARO!\n\n"
        "Выберите действие 👇",
        reply_markup=main_menu,
    )

    await callback.answer()
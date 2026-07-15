from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

plans_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⚡ 1 месяц — 199 ₽",
                callback_data="plan_1",
            )
        ],
        [
            InlineKeyboardButton(
                text="🔥 3 месяца — 499 ₽",
                callback_data="plan_3",
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 12 месяцев — 1490 ₽",
                callback_data="plan_12",
            )
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back_main",
            )
        ],
    ]
)
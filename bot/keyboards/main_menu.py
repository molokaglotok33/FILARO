from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🛒 Купить подписку",
                callback_data="buy",
            )
        ],
        [
            InlineKeyboardButton(
                text="👤 Мой профиль",
                callback_data="profile",
            )
        ],
        [
            InlineKeyboardButton(
                text="📖 Инструкция",
                callback_data="guide",
            )
        ],
        [
            InlineKeyboardButton(
                text="🆘 Поддержка",
                callback_data="support",
            )
        ],
    ]
)
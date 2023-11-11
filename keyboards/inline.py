from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

search = InlineKeyboardMarkup (
    inline_keyboard= [
        [
            InlineKeyboardButton(text = "💻 Главное меню", callback_data = "main")
        ]
    ]
)
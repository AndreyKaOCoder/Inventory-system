from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

main = ReplyKeyboardMarkup (
    keyboard= [
        [
            KeyboardButton(text = "🧾 Инвентаризация")
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True,
    input_field_placeholder = "Выберите действие из меню",
    selective = True
)

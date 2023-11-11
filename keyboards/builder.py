from aiogram.utils.keyboard import ReplyKeyboardBuilder
from handlers.inventorization_commands import inv_book

def kb_inventory():
    builder = ReplyKeyboardBuilder()
    for item in inv_book.sheetnames:
        builder.button(text = item)
    builder.adjust(3)
    builder.button(text = "💻 Главное меню")
    return builder.as_markup(resize_keyboard = True)
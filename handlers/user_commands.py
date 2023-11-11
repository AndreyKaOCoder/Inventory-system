from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import reply, builder

router = Router()

@router.message(CommandStart())
async def start (message: Message):
    await message.answer(f"💻 Бот - Система инвентаризации", reply_markup = reply.main)

@router.message(F.text.lower() == "🧾 инвентаризация")
async def inventorization (message: Message):
    await message.answer(f"👆 Выберите инвентаризацию:", reply_markup = builder.kb_inventory())

@router.message(F.text.lower() == "💻 главное меню")
async def start (message: Message):
    await message.answer(f"💻 Бот - Система инвентаризации", reply_markup = reply.main)

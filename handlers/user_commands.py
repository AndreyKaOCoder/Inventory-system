from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards import reply, builder
from utils.states import Search

router = Router()

@router.message(CommandStart())
async def comm_start (message: Message):
    await message.answer(f"💻 Бот - Система инвентаризации", reply_markup = reply.main)

@router.message(F.text.lower() == "🧾 инвентаризация")
async def comm_inventorization (message: Message):
    await message.answer(f"👆 Выберите инвентаризацию:", reply_markup = builder.kb_inventory())

@router.message(F.text.lower() == "💻 главное меню")
async def commm_start (message: Message, state: FSMContext):
    await state.clear()
    await message.answer(f"💻 Бот - Система инвентаризации", reply_markup = reply.main)

@router.message(F.text.lower() == "🔎 поиск")
async def comm_search (message: Message, state: FSMContext):
    await state.set_state(Search.index)
    await message.answer(f"🖊 Введите оборудование, которое хотите найти: (серийный номер/инвентарный/название)", reply_markup = reply.exit)

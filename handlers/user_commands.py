import requests

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from bs4 import BeautifulSoup

from keyboards import reply, builder
from utils.states import Search
from config_reader import config

router = Router()

response = requests.get(config.url.get_secret_value())

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

@router.message(F.text.lower() == "📱 информация о сайте")
async def comm_info (message: Message):
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.find('p').get_text()
    await message.answer(f"Информация с сайта:\n{text}", reply_markup = reply.main)
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Тут ты сможешь купить готовую лабораторную работу. Какой предмет интересует?", reply_markup=kb.main)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("При возникновении проблем с оплатой или дополнительных вопросов - пишите @riwaldow")

@router.message(F.text == "АИП")
async def aip(message: Message):
    await message.answer("Выберите нужную лабораторную работу", reply_markup=kb.aip)

@router.callback_query(F.data == "lab1")
async def aip1(callback: CallbackQuery):
    await callback.answer("Вы выбрали 1 лабу по аипчику")
    await callback.message.answer ("1 лаба по этой хуйне на тему Говно и залупа будет стоить 14 тысяч биткоинов на мой криптокошелек, даблю?")
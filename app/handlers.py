from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb
import app.database.requests as rq


router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Тут ты сможешь купить готовую лабораторную работу. Какой предмет интересует?", reply_markup=kb.main)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("При возникновении проблем с оплатой или дополнительных вопросов - пишите @riwaldow")

@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def category(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$')

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="АИП")],
                                     [KeyboardButton(text="Физика")],
                                     [KeyboardButton(text="ОССТ")]],
                            resize_keyboard=True,
                            input_field_placeholder="Выберите нужный предмет...")

aip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Лаб1 300р", callback_data="lab1")],
    [InlineKeyboardButton(text="Лаба2 200р", callback_data="lab2")],
    [InlineKeyboardButton(text="Максим Пидорас W", callback_data="lab3")]])
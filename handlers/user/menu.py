import keyboards.default
from loader import dp
from aiogram import types, html
from utils.misc_funcs import get_greetings


@dp.message(commands=["menu"])
async def cmd_start(message: types.Message, user_data: dict):
    text = get_start_text(user_data)
    kb = keyboards.default.main_menu.MainMenu.main_menu()
    await message.answer(text, reply_markup=kb)


def get_start_text(user_data: dict):
    text = f"{get_greetings().capitalize()}, {html.bold(html.quote(user_data['username']))}!"
    return text

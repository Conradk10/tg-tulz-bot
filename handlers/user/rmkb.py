from aiogram.dispatcher.filters import CommandObject

import keyboards.default
from loader import dp
from aiogram import types, html
from utils.misc_funcs import get_greetings


@dp.message(commands=["rmkb"])
async def cmd_start(message: types.Message, command: CommandObject, user_data: dict):
    text = get_text(user_data)
    kb = types.ReplyKeyboardRemove()
    await message.answer(text, reply_markup=kb)


def get_text(user_data: dict):
    text = f"{get_greetings().capitalize()}, клавиатура теперь убрана"
    return text

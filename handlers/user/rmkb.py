from loader import dp
from aiogram import types, html


@dp.message(commands=["rmkb"])
async def cmd_start(message: types.Message, user_data: dict):
    text = get_text(user_data)
    kb = types.ReplyKeyboardRemove()
    await message.answer(text, reply_markup=kb)


def get_text(user_data: dict):
    text = f"{html.bold(html.quote(user_data['username']))}, клавиатура теперь убрана"
    return text

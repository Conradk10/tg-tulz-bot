from loader import dp
from aiogram import types, html


@dp.message(commands=["webapp"])
async def cmd_webapp(message: types.Message, user_data: dict):
    text = get_text(user_data)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Open Webview",
                                        web_app=types.WebAppInfo(url=f"https://z-net.xyz/tg/test/example.html"))]
        ])
    await message.answer(text, reply_markup=kb)


def get_text(user_data: dict):
    text = f"{html.bold(html.quote(user_data['username']))}, отправляю тестовый WebApp"
    return text

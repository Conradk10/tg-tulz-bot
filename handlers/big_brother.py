from loader import dp
from aiogram import types, html, filters


@dp.message(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def somebody_added(message: types.Message):
    users_list = [html.link(html.quote(user.full_name), f"tg://user?id={user.id}") for user in message.new_chat_members]
    text = f"{html.link('​', 'https://i.imgur.com/bMN078b.gif')}" \
           f"🧿 {', '.join(users_list)}, приветствую тебя в чате <b>{message.chat.title}</b>! 🧿\n\n" \
           f"🕹 У нас множество ботов, игр, и развлекательных приколюх\n" \
           f"Но перед тем, как окунуться в наш мир🌏, просим ознакомиться с правилами📝 нажатием кнопки " \
           f"«📋 Правила чата» и составом админов нашего чата 😁"
    kb = None
    await message.answer(text, reply_markup=kb)


@dp.message(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def somebody_left(message: types.Message):
    user = message.left_chat_member
    await message.answer(f"{user.full_name} вышел из чата")

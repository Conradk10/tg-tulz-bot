import keyboards
from loader import dp
from magic_filter import F
from aiogram import types, html


@dp.message(commands=["rules"])
async def cmd_start(message: types.Message, user_data: dict):
    text = get_rules_text(user_data)
    kb = None
    await message.reply(text, reply_markup=kb)


def get_rules_text(user_data: dict):
    text = f"{html.link('​', 'https://i.imgur.com/M75Umz2.gif')}🗓 <b>Правила чата</b>:\n\n" \
           f"🔸 Главное - порядок и позитивная атмосфера в чате ❕\n\n️" \
           f"🔹 Флуд ботами – предупреждение, мут до 30 минут\n" \
           f"🔹 Спам, флуд, итп – предупреждение, мут до 60 минут\n" \
           f"🔹 Cпойлеры, дизинфа – предупреждение, мут до 12 часов\n" \
           f"🔹 Сомнительные ссылки – предупреждение с удалением сообщения, мут до 24 часов\n" \
           f"🔹 Злоупотребление привилегией - предупреждение, снятие с привилегии\n" \
           f"🔹 Несоглассованный пиар, реклама – предупреждение, бан\n\n" \
           f"⚜️ Остальные нарушения на усмотрение админов 😎\n" \
           f"❗️ Уведомить о нарушении – @admin"
    return text

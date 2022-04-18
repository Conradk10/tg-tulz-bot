import requests
import datetime
from rich import print
from aiogram import types, html
""" Основные функции бота """


async def get_full_user_data(user_data: dict) -> dict:
    """ Дополняет данные юзера из БД """
    user_data['deeplink'] = html.link(html.quote(user_data['username']), f"tg://user?id={user_data['uid']}")
    user_data['regdate'] = user_data['regtime'].strftime("%d.%m.%Y")
    return user_data


def send_logs(message: types.Message = None, callback_query: types.CallbackQuery = None, error=False) -> None:
    """ Распечатывает логи в терминал """
    if message:
        data = [message.from_user.id, message.from_user.full_name, message.chat.title, message.text,
                message.message_id]
    elif callback_query:
        data = [callback_query.from_user.id, callback_query.from_user.full_name, callback_query.message.chat.title,
                callback_query.data, callback_query.message.message_id]
    else:
        return
    uid, fullname, chat_name, text, message_id = data
    if chat_name is None:
        chat_name = "PM"
    if error: error = "red"
    else: error = "white"
    print(f'[green bold]{datetime.datetime.now()}[/green bold] | [yellow bold]{chat_name} - ({uid}) [/yellow bold]'
          f'[{error} bold]{fullname}[/{error} bold][yellow bold] -> [/yellow bold][{error} bold]{text} [/{error} bold]'
          f'[yellow bold]({message_id})')

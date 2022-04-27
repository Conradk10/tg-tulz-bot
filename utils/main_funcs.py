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


def send_logs(message: types.Message, error=None) -> None:
    """ Распечатывает логи в терминал """
    if error: error = "red"
    else: error = "white"
    print(f'[green bold]{datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")}[/green bold] | [yellow bold]'
          f'{message.chat.id or "PM"} ({message.chat.title}) – ({message.from_user.id}) [/yellow bold]'
          f'[{error} bold]{message.from_user.full_name}[/{error} bold][yellow bold] → [{error} bold]'
          f'{message.text or message.content_type} [/{error} bold]({message.message_id})')

# - *- coding: utf- 8 - *-
import datetime
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, types, html

from loader import bot
from utils.db_api.sqliter import get_free_sql
from utils.main_funcs import send_logs, get_full_user_data
from utils.misc_funcs import to_fixed


class BigBrotherMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(self, handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
                       event: types.Message, data: Dict[str, Any]) -> Any:

        # await bot.send_chat_action(event.chat.id, 'typing')

        user_data = get_free_sql("select * from users where uid = %s", (event.from_user.id,))
        if user_data is None:
            get_free_sql("insert into users (uid, username) values (%s, %s)",
                         (event.from_user.id, event.from_user.full_name))
            user_data = get_free_sql("select * from users where uid = %s", (event.from_user.id,))

        if user_data['username'] != event.from_user.full_name:
            get_free_sql("update users set username = %s where uid = %s",
                         (event.from_user.full_name, event.from_user.id))
            user_data['username'] = event.from_user.full_name

        user_data = await get_full_user_data(user_data)

        data['user_data'] = user_data
        send_logs(message=event)
        return await handler(event, data)

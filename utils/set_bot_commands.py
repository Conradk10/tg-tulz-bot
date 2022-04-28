from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    """ Устанавливает команды бота """
    commands = [BotCommand(command="start", description="🚀 Запуск"),
                BotCommand(command="rules", description="🗓 Правила чата"),
                BotCommand(command="rmkb", description="📱 Убрать клавиатуру")]
    await bot.set_my_commands(commands=commands)

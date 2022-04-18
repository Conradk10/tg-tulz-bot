from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


async def set_bot_commands(bot: Bot):
    """ Устанавливает команды бота """
    commands = [BotCommand(command="start", description="🚀 Запуск/помощь"),
                BotCommand(command="rules", description="🗓 Правила чата"),
                BotCommand(command="rules", description="📱 Главное меню")]
    await bot.set_my_commands(commands=commands)

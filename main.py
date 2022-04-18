from rich import print
from loader import bot, dp
from utils.db_api.sqliter import connection
from utils.set_bot_commands import set_bot_commands


async def on_startup():
    print("[bold yellow]🔄 Загрузка...")
    import handlers
    import middlewares
    middlewares.setup(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await set_bot_commands(bot)
    print("[bold green]✅ Бот успешно запущен!")


async def on_shutdown():
    print("[bold yellow]🔄 Остановка...")
    connection.close()
    print("[bold green]✅ Бот успешно остановлен!")


if __name__ == "__main__":
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.run_polling(bot)

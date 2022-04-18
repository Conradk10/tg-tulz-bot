from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from currency_converter import CurrencyConverter
from data import config

curr = CurrencyConverter()
bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

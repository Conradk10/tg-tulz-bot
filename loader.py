from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage
from instagrapi import Client
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

ig_client = None
# ig_client = Client()
# ig_client.login(config.instagram["login"], config.instagram["password"])

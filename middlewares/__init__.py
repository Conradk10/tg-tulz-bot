from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware
from .big_brother import BigBrotherMiddleware


def setup(dp: Dispatcher):
    dp.message.middleware(ThrottlingMiddleware())
    dp.message.middleware(BigBrotherMiddleware())

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import BaseStorage
# from aiogram.fsm.storage.redis import RedisStorage
from bot.routers.basic import r as base_router

from settings.config import settings


async def bot_startup():
    bot = Bot(
        token=settings.TG_API,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    storage = None  # RedisStorage.from_url('redis://localhost:6379/0')
    dp = Dispatcher()

    dp.include_routers(
        base_router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(bot_startup())

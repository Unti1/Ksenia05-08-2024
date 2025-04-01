from aiogram import F, Router
from aiogram.types import Message

r = Router()

@r.message()
async def start_message(message: Message):
    # print(message)
    # print(message.text)
    await message.answer('Привет! Чем могу помочь?')
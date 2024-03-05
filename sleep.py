from config import token
from rich import print
import asyncio

from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token)
dp = Dispatcher()



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer('Бот скоро заработает. Мы "делаем все" чтоб оно работал')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
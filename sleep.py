from config import token, bot_commands

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token, parse_mode='html')
dp = Dispatcher()


@dp.message()
async def echo(message: Message):
    await message.answer("⚙️Бот чиниться🛠")

async def main():

    await bot.set_my_commands(bot_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=bot_commands)



if __name__ == "__main__":
    print("BOT SLEEP")
    asyncio.run(main())

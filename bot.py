from config import token, bot_commands
from rich import print
import asyncio

from handlers import user_comands

from aiogram import Bot, Dispatcher
6499796708:AAEHbmOSUdRC1mzSmltSrHAxqlWscNBPceg

async def main():
    bot = Bot(token, parse_mode='html')
    dp = Dispatcher()

    dp.include_routers(
        user_comands.router,
    )

    await bot.set_my_commands(bot_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=bot_commands)



if __name__ == "__main__":
 
    print("[cyan1 blink bold]Bot work[/cyan1  blink bold]")
    asyncio.run(main())

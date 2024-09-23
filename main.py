import aiogram 
import logging
import os
from aiogram import Bot, Dispatcher,types
import asyncio
from basic import router
from connection import dp, bot
from aiogram.filters import CommandStart, Command



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        


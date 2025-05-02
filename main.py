import asyncio
from aiogram import Bot, Dispatcher, types
import asyncio

API_TOKEN = '7621464920:AAGGIg20gP_cLWeGo6o-7BHwClNwmY_bsdM'  # <-- в кавычках!

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

API_TOKEN = 'ТВОЙ_ТОКЕН'

bot = Bot(
7621464920:AAGGIg20gP_cLWeGo6o-7BHwClNwmY_bsdM)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer(
        "Я рядом, когда саду нужна помощь.\n"
        "Я вижу, как живет ваш сад и помогаю сохранить то, что в нем важно.\n"
        "У каждого сада — свой путь.\n"
        "Моя задача — пройти его вместе с вами: внимательно, честно, с уважением к каждому листику.\n"
        "Откройте памятку — и начните слышать свой сад по-настоящему."
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = "7621464920:AAGGIg20gP_cLWeGo6o-7BHwClNwmY_bsdM
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 Купить гайд за 1800 ₽")],
            [KeyboardButton(text="ℹ️ Помощь")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        "Добро пожаловать в Зелёный Доктор! 🌱\n\nВыберите действие:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "💰 Купить гайд за 1800 ₽")
async def buy_guide_handler(message: Message):
    await message.answer("Чтобы купить гайд за 1800 ₽, нажмите на кнопку оплаты или свяжитесь с поддержкой.")

@dp.message(lambda message: message.text == "ℹ️ Помощь")
async def help_handler(message: Message):
    await message.answer("Я помогу вашему саду быть здоровым. 🌿 Просто выберите действие из меню.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


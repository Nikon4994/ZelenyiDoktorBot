import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio

API_TOKEN = "7621464920:AAGRn_2z8GLUyEdGZ6tS-_EoYpa_HiaMvPI"
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
    await message.answer(
    "🌿 Добро пожаловать в «Зелёный Доктор»!\n\n"
    "Здесь вы найдёте профессиональные памятки (гайды) по уходу за растениями:\n"
    "— Как защитить сад от болезней и вредителей\n"
    "— Как правильно ухаживать за хвойными, декоративными и плодовыми\n"
    "— Как поддерживать сад здоровым весь сезон\n"
    "— Какие препараты и подкормки реально работают\n\n"
    "📚 Чтобы получить памятку — нажмите кнопку «Купить гайд»."
)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


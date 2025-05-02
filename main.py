import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Твой токен
API_TOKEN = '7621464920:AAGGIg20gP_cLWeGo6o-7BHwClNwmY_bsdM'

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаём объекты бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Я рядом, когда саду нужна помощь.\n"
        "Я вижу, как живет ваш сад и помогаю сохранить то, что в нем важно.\n"
        "У каждого сада — свой путь.\n"
        "Моя задача — пройти его вместе с вами: внимательно, честно, с уважением к каждому листку.\n"
        "Откройте памятку — и начните слышать свой сад по-настоящему."
    )

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

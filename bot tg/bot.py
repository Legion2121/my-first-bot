import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8749346436:AAEOzh9RAXzra1A_F0LHtGL-p1swuKbmjME"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="💅 Записаться")],
            [types.KeyboardButton(text="💸 Цены")],
            [types.KeyboardButton(text="📍 Адрес")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Привет! Я помощник салона 💅\nВыбери действие:",
        reply_markup=keyboard
    )

@dp.message()
async def handler(message: types.Message):
    text = message.text

    if text == "💅 Записаться":
        await message.answer("Напиши удобное время, и я запишу тебя ✍️")

    elif text == "💸 Цены":
        await message.answer("Маникюр — 1500₽ 💅\nПедикюр — 2000₽")

    elif text == "📍 Адрес":
        await message.answer("Мы находимся в центре города 📍")

    else:
        await message.answer("Используй кнопки ниже 👇")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
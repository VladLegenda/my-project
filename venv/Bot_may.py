import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio
import os



TOKEN = os.getenv('TOKEN')
logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


cyrillic = (
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
)
latin = (
    'ABVGDEEJZIIKLMNOPRSTUFHCCHHYIEUYA'
    'abvgdeejziiklmnoprstufhcchhyieuya'
)


if len(cyrillic) != len(latin):
    raise ValueError("Длины строк cyrillic и latin должны быть одинаковыми!")

# Создаем таблицу перевода
translit_table = str.maketrans(cyrillic, latin)

def transliterate(name):
    return name.translate(translit_table)

@dp.message(Command(commands=['start']))
async def user_name_lastname(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}, давайте узнаем ваше ФИО!'
    logging.info(f'{user_name} {user_id} запустил бота')
    await message.answer(text)

@dp.message(Command(commands=['help']))
async def help_command(message: types.Message):
    await message.answer("Отправьте ваше ФИО в кириллице, и я преобразую его в латиницу.")

@dp.message()
async def enter_your_name(message: types.Message):
    full_name = message.text.strip()
    transliterated_name = transliterate(full_name)
    await message.answer(f'Ваше ФИО на латинице: {transliterated_name}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.info("Бот запущен!")
    asyncio.run(main())


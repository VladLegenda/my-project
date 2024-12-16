import logging

from aiogram import Bot, Dispatcher
from aiogram.types import Message  # ловим обновления этого типа
from aiogram.filters.command import Command  # обрабатываем команды /start, /help, и другие


# Инициализация объекта
bot = Bot(token='7722450713:AAGArVSOdB-WU-Tr6jJ9vfQLsANsanW9w8U')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

# Обработка команды start
@dp.message(Command(commands=['start']))

async def procces_command_start(message: Message):  # Функция по обработке команды старт с помощью класса Message(ассинхронная функция)
    user_name = message.from_user.full_name  # Узнаем имя пользователя
    user_id = message.from_user.id    # узнаём айди пользователя
    text = f'Привет, {user_name}!'    # Текст приветсвия
    logging.info(f'{user_name} {user_id} запустил бота') # чтобы увидеть кто запускал бота
    await bot.send_message(chat_id=user_id, text=text)  # Отправляем сообщение в наш чат(await используется в ассинхронных функциях вместо return)
    

# Обработка всех сообщений
@dp.message()
async def send_echo(message: Message):  # Функция по обработке всех сообщений
    user_name = message.from_user.full_name  # Узнаем имя пользователя
    user_id = message.from_user.id    # узнаём айди пользователя
    text = message.text    # Текст 
    logging.info(f'{user_name} {user_id}: {text}') # чтобы увидеть кто запускал бота
    await message.answer(text=text)  # Отправляем сообщение в наш чат(await используется в ассинхронных функциях вместо return)   


    # Запускаем процесс пуллинга
if __name__ == '__main__':
    dp.run_polling(bot) # Отслеживает обновления всё что касается нашего бота
    



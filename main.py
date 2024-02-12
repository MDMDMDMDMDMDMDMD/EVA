import asyncio
import openai

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message

import keyboards
from ChatGPT import gpt

bot = Bot("")
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет! Чем я могу тебе помочь?")


@dp.message(Command("restart"))
async def restart(message: Message):
    await message.answer(f"Начинаем с чисто листа")


@dp.message(Command("about"))
async def about(message: Message):
    await message.answer(f"Ева это бот созданный @EvaaaDev")


@dp.message(Command("help"))
async def hellp(message: Message):
    await message.answer(f"Я могу ответиь на любой твой вопрос")


@dp.message()
async def send(message: Message):
    await message.answer('Генерируется ответ♻️')  # Даём понять пользователю, что бот работает
    await message.reply(gpt(message.text))
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id + 1)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
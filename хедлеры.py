from aiogram import Bot, Dispacher, executor, types
from aiogram.contrid.fsm_storage.memory import MemoryStorage
import asyncio

api_key = 7814985248
bot = Bot(token=api_key)
dsp = Dispacher(bot=bot, storage=MemoryStorage())

@dsp.massage_handler(commands=['start'])
async def start(message):
    print('Привет! я -- бот помогающий твоему здоровью')

@dsp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)
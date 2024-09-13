from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the Flower Delivery Bot!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
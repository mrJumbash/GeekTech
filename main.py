from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging


TOKEN = config('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,  f'Hello, {message.from_user.first_name}')

    await message.answer('This is answer method!')

    await message.reply('This is reply answer!')

@dp.message_handler(commands=['quiz_1'])
async def quiz_1(message: types.Message):
    question = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]

    await bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="IZI",
        open_period=60,
    )

@dp.message_handler(commands=['quiz_2'])
async def quiz_2(message: types.Message):
    question = "By whom invented Rust?"
    answers = [
        "Dennis Ritchie",
        "Graydon Hoare",
        "Guido Van Rossum",
        "Robert Griesemer",
    ]

    await bot.send_poll(
        message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Software developer Graydon Hoare created Rust as a personal project while working at Mozilla "
                    "Research in 2006.",
        open_period=120,
    )

@dp.message_handler(commands=['meme_1'])
async def start_command(message: types.Message):
    await message.answer_photo(open('/home/kuba/Pictures/shrek.jpeg', 'rb'), caption="Shrek")
    await message.delete()

@dp.message_handler(commands=['meme_2'])
async def start_command(message: types.Message):
    await message.answer_photo(open('/home/kuba/Pictures/villager.jpeg', 'rb'), caption="MineVillagerStonks")
    # await message.delete()

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text)**2)
    else:
        await bot.send_message(message.from_user.id,  message.text)



if  __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,  skip_updates=True, )
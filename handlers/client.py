from config import bot, ADMINS
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.client_kb import start_markup

async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,  f'Hello, {message.from_user.first_name}',
                           reply_markup=start_markup)

    # await message.answer('This is answer method!')
    #
    # await message.reply('This is reply answer!')


async def quiz(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    button_call_2 = InlineKeyboardButton('NEXT-2', callback_data='button_call_2')
    button_call_3 = InlineKeyboardButton('NEXT-3', callback_data='button_call_3')

    markup.add(button_call_1, button_call_2, button_call_3)


    question = "By whom invented Rust?"
    answers = [
        "Dennis Ritchie",
        "Graydon Hoare",
        "Guido Van Rossum",
        "Robert Griesemer",
    ]

    await bot.send_poll(
        message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Software developer Graydon Hoare created Rust as a personal project while working at Mozilla "
                    "Research in 2006.",
        open_period=120,
        reply_markup=markup,
    )


# async def start_command(message: types.Message):
#     await message.answer_photo(open('/home/kuba/Pictures/shrek.jpeg', 'rb'), caption="Shrek")
#     await message.delete()
#
# async def start_command(message: types.Message):
#     await message.answer_photo(open('/home/kuba/Pictures/villager.jpeg', 'rb'), caption="MineVillagerStonks")
#     # await message.delete()

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands='start')
    dp.register_message_handler(quiz, commands='quiz')

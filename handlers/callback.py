from config import bot, Dispatcher
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('NEXT', callback_data='button_call_2')
    markup.add(button_call_2)

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
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="IZI",
        open_period=60,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):

    question = "By whom Harry Potter was written?"
    answers = [
        "JK Rowling",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]

    await bot.send_poll(
        call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
        explanation="IZI",
        open_period=60,

    )


async def quiz_stop(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('NEXT', callback_data='button_call_3')
    markup.add(button_call_3)
    shrek_stop = open('media/shrek.jpeg', 'rb')
    await bot.send_photo(call.message.chat.id, shrek_stop, reply_markup=markup)
    await bot.send_message(call.message.chat.id, "Остановочка ('-')")

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_stop, text='button_call_2')
    dp.register_callback_query_handler(quiz_3, text='button_call_3')
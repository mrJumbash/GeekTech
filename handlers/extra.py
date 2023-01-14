from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice

async def echo(message: types.Message):
    bad_words = ['java', 'html', 'дурак', "дура"]
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.first_name
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            # DRY - Don't Repeat Yourself
            await message.answer(f"Не матерись {username}"
                                 f" сам ты {word}!")
    if message.from_user.id in ADMINS:
        emoji_list = ['⚽️', '🏀', '🎲', '🎰', '🎯', '🎳']
        emoji = choice(emoji_list)
        if message.text == 'game':
            await bot.send_dice(message.chat.id, emoji=emoji)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
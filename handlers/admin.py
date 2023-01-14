from aiogram import types, Dispatcher
from config import bot, ADMINS



async def dice_game(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer('Ur turn:')
        users_points = await bot.send_dice(message.chat.id)
        await message.answer('And my turn:')
        bots_points = await bot.send_dice(message.chat.id)
        if users_points.dice.value > bots_points.dice.value:
            await message.answer('U won!')
        elif users_points.dice.value < bots_points.dice.value:
            await message.answer('I won!')
        else:
            await message.answer('MEH')

async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должны быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")

    else:
        await message.answer("Пиши в группу!")

async def pin(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должны быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer("Пиши в группу!")


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(dice_game, commands=['dice'], commands_prefix='!/')

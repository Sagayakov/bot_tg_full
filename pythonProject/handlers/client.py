from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db

async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятно познакомиться', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишите ему:\nhttps://t.me/satka_smart_bot')


async def bot_open_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ПН - Пт с 10:00 до 18:00, СБ-ВС по предварительной записи')


async def bot_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'ул. Свободы 10')


async def bot_price_command(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(bot_open_command, commands=['Режим_работы'])
    dp.register_message_handler(bot_place_command, commands=['Расположение'])
    dp.register_message_handler(bot_price_command, commands=['Прайс'])
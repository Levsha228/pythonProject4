from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType
from QtBot import MainWindow

bot_token = '5973256978:AAEy_YK5UHXGg0Vrq7UGjy7WJBWyp75vjYA'
test_bot_token = '5973256978:AAEy_YK5UHXGg0Vrq7UGjy7WJBWyp75vjYA'
chat_id_me = 538393324
chat_id_group = -798451609
chat_id_ilya = 979056570
chat_id_dasha = 534198136
bot = Bot(token=bot_token)
dp = Dispatcher()
bot_id = 5809889046
OWNER_ID = 979056570
msg = 'Privet'
btn_clck = True

@dp.message()
async def button_click(message: Message):
    global btn_clck
    #if btn_clck == True:
    await bot.send_message(chat_id_group, msg)
    btn_clck = False

dp.run_polling(bot)

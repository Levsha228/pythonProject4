import SqlManagerTableUsers
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message, ContentType
from translate import Translator
import time
#Ghbdrtdtg
translator = Translator(to_lang='ru')
weatherbot_token = '5909589595:AAFj5H0gQ-he2rdHU9oqaA2fs4CR6q_z3dg'
manager_of_world_bot_token = '5809889046:AAFowyM52dvYoplUA3x7PBvrp1Gc6q4nmpg' # MAIN!!!
test_bot_token = '5815945380:AAHpSmPV0GhZu8NQYAN_75v3jHSOQFVvbxE'
bot = Bot(token=manager_of_world_bot_token)
dp = Dispatcher()
bot_id = 5809889046
OWNER_ID = 979056570
flag = True

@dp.message(Command(commands=['menu']))
async def process_start_command(message: Message):
    print('wqeqw')

@dp.message(Command(commands=['dbstart']))
async def db_start(message: Message):
    global flag
    flag = True
@dp.message(Command(commands=['dbstop']))
async def db_start(message: Message):
    global flag
    flag = False
@dp.message()
async def action_with_table_users(message: Message):
    if message.chat.type != 'private' and flag == True:
        sql_table = SqlManagerTableUsers.TableManager()
        if sql_table.get_user_info(message.from_user.id) != False:
            # Порядок заполненности (get_user_info):
            # [0]-user_id, [1]-date_time_UTC, [2]-user_name, [3] date_in_seсonds, [4] - chat_id,
            # [5] - deletion_warning_time
            sql_table.update_last_aktivity(message.from_user.id, message.chat.id)
        else:
            sql_table.add_user(message.from_user.id, message.from_user.username, message.chat.id)
            await message.answer(f'{message.from_user.first_name} улыбайся, тебя только что добавили в базу данных!')
        for user_id_name_chat in sql_table.find_not_active_users(message.chat.id):
            await message.answer(f"{user_id_name_chat[1]} подлежит удалению из чата")
            await message.answer(f"@{user_id_name_chat[1]}, Я УДАЛЮ ТЕБЯ ИЗ ГРУППЫ если ничего не напишешь!\nУ тебя "
                                 f"есть 24 часа!")
        for user in sql_table.list_of_users_to_remove():  # [0]-id, [1]-user_name
            await bot.send_message(message.chat.id, f"{user[1]} Именем Господнем, я изгоняю тебя из чата!")
            await bot.kick_chat_member(message.chat.id, user[0])


dp.run_polling(bot)

import telebot
from telebot import types
import requests
import pprint
import json
import random



token = '5973256978:AAEy_YK5UHXGg0Vrq7UGjy7WJBWyp75vjYA'
api_url =  '  https://inshorts.deta.dev/news?category=science'
response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response
r = random.randint(0,5)
if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    pprint.pprint(response.text)
else:
    print(response.status_code)    #
with open("data_file.json", "w") as f:
    f.write(response.text)
with open("data_file.json","r") as f1:
    data = json.load(f1)
print(data['data'][r]['content'])


bot=telebot.TeleBot(token)
@bot.message_handler(content_types='text') #создаем команду
def start(message):
    if message.text == 'наука':
        rand = random.randint(0, 5)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Мой раб", url='https://t.me/ilya88005553535')
        markup.add(button1)
        bot.send_message(message.chat.id, f"Все говорят: {data['data'][rand]['content']}, а ты купи Слона!", reply_markup=markup)

bot.infinity_polling()
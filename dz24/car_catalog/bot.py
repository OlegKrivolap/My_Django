import os
from dotenv import load_dotenv
from pathlib import Path
from telebot import TeleBot
load_dotenv()

bot = TeleBot(os.getenv('TELEGRAM_BOT_API_KEY'), threaded=False)



def bot_save():
    bot.send_message(chat_id='@channej_dj', text='Были добавлены данные')
    print('hi')


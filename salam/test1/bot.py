import os
from dotenv import load_dotenv
from pathlib import Path
from telebot import TeleBot
dotenv_path = Path('salam/.env')
load_dotenv(dotenv_path=dotenv_path)

bot = TeleBot(os.getenv('TELEGRAM_BOT_API_KEY'), threaded=False)



def bot_save():
    bot.send_message(chat_id='@channej_dj', text='Были добавлены данные')


def bot_delete():
    bot.send_message(chat_id='@channej_dj', text='Были удалены данные')

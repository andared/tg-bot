import logging

import telebot
import tg_logger
from flask import Flask
from settings import Settings

# ------------- bot -------------
bot = telebot.TeleBot(Settings.BOT_TOKEN)

# ------------- flask app -------------
app = Flask(__name__)

# ------------- logging -------------
logger = logging.getLogger("tg-bot-template")

alpha_logger = logging.getLogger()
alpha_logger.setLevel(logging.INFO)

"""
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
"""
app.logger.setLevel(logging.ERROR)
telebot.logger.setLevel(logging.ERROR)

users = [Settings.ADMIN_ID]

if Settings.LOG_BOT_TOKEN != '':
    tg_logger.setup(alpha_logger, token=Settings.LOG_BOT_TOKEN, users=users)
    tg_logger.setup(app.logger, token=Settings.LOG_BOT_TOKEN, users=users)
    tg_logger.setup(telebot.logger, token=Settings.LOG_BOT_TOKEN, users=users)

# ------------- webhook -------------
ADMIN_PASSWORD = Settings.ADMIN_PASSWORD
WEBHOOK_TOKEN = Settings.WEBHOOK_TOKEN

#  Copyright (c) ChernV (@otter18), 2021.

import random

from setup import bot, logger
from webhook import app
from settings import Settings

# --------------- dialog params -------------------
dialog = {
    'hello': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey', 'прив'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!', 'Добрый день!']
    },
    'how r u': {
        'in': ['как дела', 'как ты', 'how are you', 'дела', 'how is it going', 'как сам'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['зовут', 'name', 'имя', 'кто'],
        'out': [
            'Я telegram-bot Андрея',
            'Я бот шаблон, но ты можешь звать меня в свой проект',
            'Это секрет. Используй команду /help, чтобы узнать'
        ]
    }
}


# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start', 'info'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        'Hello! This is a telegram bot written by @ryabokonnnn'
    )


@bot.message_handler(commands=['zakaz', 'order'])
def make_order(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /zakaz or /order')
    bot.send_message(
        message.chat.id,
        '<b>Для оформления заказа, пожалуйста, напишите @multikate с указанием товара, который необходимо приобрести.'
        'Либо оформите его по ссылке - <a href="https://shop.9282922.ru/catalog/kompyutery/apple_macbook_air_13_retina_mly33_midnight_m2_8_core_gpu_8_core_8_gb_256_gb/">macbook</a></b>',
        parse_mode="html"
    )


@bot.message_handler(func=lambda message: True)
def echo(message):
    for t, resp in dialog.items():
        if sum([e in message.text.lower() for e in resp['in']]):
            logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used {t}:\n\n%s', message.text)
            bot.send_message(message.chat.id, random.choice(resp['out']))
            return

    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used echo:\n\n%s', message.text)
    bot.send_message(
        message.chat.id,
        text="Unknown command, use /help"
    )


if __name__ == '__main__':
    if Settings.IS_PRODUCTION == "True":
        app.run()
    else:
        bot.infinity_polling()

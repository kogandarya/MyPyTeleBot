import random
import telebot
from telebot import types
import logging

API_TOKEN = '5140356079:AAF_iCBF6uxs-2FFRMvWbQ39SHpUCdv5P48'

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.INFO)

storage = dict()

def init_storage(user_id):
    storage[user_id] = dict(attempt=None, random_digit=None)

def set_data_storage(user_id, key, value):
    storage[user_id][key] = value

def get_data_storage(user_id):
    return storage[user_id]

@bot.message_handler(func=lambda message: message.text.lower() == "игра")
def digitgames(message):
    init_storage(message.chat.id)

    attempt = 5
    set_data_storage(message.chat.id, "attempt", attempt)

    bot.send_message(message.chat.id, f'Игра "угадай число"!\nКоличество попыток: {attempt}')

    random_digit = random.randint(1, 10)
    print(random_digit)

    set_data_storage(message.chat.id, "random_digit", random_digit)
    print(get_data_storage(message.chat.id))

    bot.send_message(message.chat.id, 'Готово! Загадано число от 1 до 10!')
    bot.send_message(message.chat.id, 'Введите число')
    bot.register_next_step_handler(message, process_digit_step)

def process_digit_step(message):
    user_digit = message.text

    if not user_digit.isdigit():
        msg = bot.reply_to(message, 'Вы ввели не цифры, введите пожалуйста цифры')
        bot.register_next_step_handler(msg, process_digit_step)
        return

    attempt = get_data_storage(message.chat.id)["attempt"]
    random_digit = get_data_storage(message.chat.id)["random_digit"]

    if int(user_digit) == random_digit:
        bot.send_message(message.chat.id, f'Ура! Ты угадал число! Это была цифра: {random_digit}')
        init_storage(message.chat.id)
        return
    elif attempt > 1:
        attempt -= 1
        set_data_storage(message.chat.id, "attempt", attempt)
        bot.send_message(message.chat.id, f'Неверно, осталось попыток: {attempt}')
        bot.register_next_step_handler(message, process_digit_step)
    else:
        bot.send_message(message.chat.id, 'Вы проиграли!')
        init_storage(message.chat.id)
        return

if __name__ == '__main__':
    bot.skip_pending = True
    bot.polling()

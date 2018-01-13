# -*- coding: utf-8 -*-

import telebot
import state
import config
import dbworker

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(message):
    current_state = dbworker.get_current_state(message.chat.id)
    if current_state == state.States.S_ENTER_NAME.value:
        bot.send_message(message.chat.id, "Отправь, пожалуйста, свое имя.")
    elif current_state == state.States.S_ENTER_AGE.value:
        bot.send_message(message.chat.id, "Скажи, пожалуйста, свой возраст.")
    elif current_state == state.States.S_ENTER_SEX.value:
        bot.send_message(message.chat.id, "Соообщи, пожалуйста, свой пол (букву \"м\" или \"ж\").")
    elif current_state == state.States.S_SEND_USER.value:
        bot.send_message(message.chat.id, "Кажется, я должен был отправить тебе один из вариантов... ")
    else:
        bot.send_message(message.chat.id, "Привет! Я бот купидон. Работаю исключительно с мифистами. Давай начнем. Как тебя зовут?")
        dbworker.set_state(message.chat.id, state.States.S_ENTER_NAME.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == state.States.S_ENTER_NAME.value)
def change_name(message):
    bot.send_message(message.chat.id, "Очень красивое имя, запомню! Теперь укажи, пожалуйста, свой пол: отправь мне букву \"м\" или \"ж\".")
    dbworker.set_state(message.chat.id, state.States.S_ENTER_SEX.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == state.States.S_ENTER_SEX.value)
def change_sex(message):
    if message.text.lower() not in ['м', 'ж']:
        bot.send_message(message.chat.id, "Пожалуйста, отправь мне букву \"м\" или \"ж\".")
        return
    else:
        bot.send_message(message.chat.id, "Хорошо. Теперь укажи, пожалуйста, свой возраст.")
        dbworker.set_state(message.chat.id, state.States.S_ENTER_AGE.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == state.States.S_ENTER_AGE.value)
def change_age(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Возраст должен быть числом (какая неожиданность) от 16 до 29 (включительно).")
        return
    if int(message.text) <= 15:
        bot.send_message(message.chat.id, "Нельзя, 134 статья УК РФ...")
        return
    if int(message.text) >= 30:
        bot.send_message(message.chat.id, "Введи, пожалуйста, корректный возраст (от 16 до 29 лет включительно).")
        return
    else:
        bot.send_message(message.chat.id, "Отлично! Когда будешь готов, вызови команду /yeah")
        dbworker.set_state(message.chat.id, state.States.S_WAIT.value)


@bot.message_handler(commands=["yeah"])
def play(message):
    bot.send_message(message.chat.id, "Игра!!")


if __name__ == "__main__":
    bot.polling(none_stop=True)
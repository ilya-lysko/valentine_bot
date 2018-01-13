import config
import telebot

bot = telebot.TeleBot(config.token)

markup = telebot.types.ReplyKeyboardMarkup()
markup.row('Yes', 'No')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def make_choice(message):
    bot.send_message(message.chat.id, 'Make your choice:', reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
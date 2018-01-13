import config
import state
import telebot

bot = telebot.TeleBot(config.token)
current_state = state.States.S_ENTER_NAME.value
markup = telebot.types.ReplyKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start(message):
	"""
	Регистрация нового пользователя, после нажатия кнопки "Start"
	"""
	current_state = state.States.S_START
	bot.send_message(message.chat.id, 'Привет, я бот-купидон для мифистов.\nКак тебя зовут?')
	current_state = state.States.S_ENTER_NAME.value
	
@bot.message_handler(func=lambda message: current_state == state.States.S_ENTER_NAME.value)
def change_name(message):
    # пока просто перешлем пользователю его же имя
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Отличное имя, запомнил! Теперь укажи, пожалуйста, свой пол.")
    current_state = state.States.S_ENTER_SEX.value

@bot.message_handler(func=lambda message: current_state == state.States.S_ENTER_SEX.value)
def change_sex(message):
    current_state = state.States.S_ENTER_SEX.value
    markup.row('муж.', 'жен.')
    if message.text in ['муж.','жен.']:
    	# пока просто перешлем пол пользователю
    	bot.send_message(message.chat.id, message.text)
    	markup = telebot.types.ReplyKeyboardMarkup()
    	current_state = state.States.S_ENTER_AGE.value
    else:
        pass
        # тут нужно вообще что-то?

@bot.message_handler(func=lambda message: current_state == state.States.S_ENTER_AGE.value)
def change_age(message):
    if message.text.isdigit() and 30 > int(message.text) >= 16:
        # пока просто перешлем пользователю его возраст
        bot.send_message(message.chat.id, message.text)
        bot.send_message(message.chat.id, 'Когда будешь готов, введи команду /help.')
        current_state = state.States.S_SEND_USER.value
    else:
        bot.send_message(message.chat.id, 'Возраст должен быть числом от 16 до 29 (включительно). Давай еще раз.')

@bot.message_handler(commands=['game'])
def game(message):
	"""
	Сам процесс подбора партнеров и сбора ответов
	"""
	bot.send_message(message.chat.id, 'Игра', reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
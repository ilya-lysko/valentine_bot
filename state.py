from enum import Enum

class States(Enum):
	"""
	Enum для состояний беседы
	"""
	S_START = "0" # Начало беседы
	S_ENTER_NAME = "1" # Ввод имени
	S_ENTER_AGE = "2" # Ввод возраста
	S_ENTER_SEX = "3" # Ввод пола
	S_SEND_USER = "4" # Подбор партнера
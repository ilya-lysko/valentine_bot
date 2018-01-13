# -*- coding: utf-8 -*-

# from vedis import Vedis
import config

def get_current_state(user_id):
    with open("file.txt", 'r') as f:
        return f.read()

def set_state(user_id, value):
    with open("file.txt", 'w') as f:
        f.write(value)

# def get_current_state(user_id):
#     with Vedis(config.db_file) as db:
#         try:
#             return db[user_id]
#         except KeyError:  # Если такого ключа почему-то не оказалось
#             return config.States.S_START.value  # значение по умолчанию - начало диалога


# def set_state(user_id, value):
#     with Vedis(config.db_file) as db:print(get_current_state(1))
#         try:
#             db[user_id] = value
#             return True
#         except:
#             # тут желательно как-то обработать ситуацию
#             return False
from telebot import types

def choise():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    usd_button = types.KeyboardButton('USD')
    eur_button = types.KeyboardButton('EUR')

    kb.add(usd_button, eur_button)

    return kb
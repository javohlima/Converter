import telebot
import buttons


bot = telebot.TeleBot('1qrdhar124ha')

USD = 11520
EUR = 12300

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Выберите валюту!', reply_markup=buttons.choise())

def usd_convert(message):
    try:
        bot.send_message(message.from_user.id, f'{int(message.text)}' / USD, reply_markup=buttons.choise())

    except telebot.apihelper.ApiTelegramException:
        bot.send_message(message.form_user.id, 'Пишите цифры!')
        bot.register_next_step_handler(message, usd_convert)

def eur_convert(message):
    try:
        bot.send_message(message.from_user.id, f'{int(message.text)}' / EUR, reply_markup=buttons.choise())

    except telebot.apihelper.ApiTelegramException:
        bot.send_message(message.form_user.id, 'Пишите цифры!')
        bot.register_next_step_handler(message, eur_convert)

bot.polling(non_stop=True)
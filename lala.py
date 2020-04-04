import telebot

bot = telebot.TeleBot('1291448630:AAEhqveigj5qThWB9Z7Tj2wmGwF19JlVz6k')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\n Я - <b>Savannah-бот</b> для входа в страницу <b>SAVANNAH</b>.\nХочешь попать в <b>SAVANNAH</b>?'.format(message.from_user), parse_mode='html')

@ bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'музыка':
        bot.send_message(message.chat.id, 'https://t.me/joinchat/AAAAAEsOj7NX9aLgxGRCNQ')
    else:
        bot.send_message(message.chat.id, message.text)

bot.polling()
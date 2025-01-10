import telebot
import webbrowser

bot = telebot.TeleBot('8119487324:AAGmBJ2Hf2nG6oK3KZaja7OqsmIzTJopmqU')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://img.freepik.com/premium-photo/stylized-letter-quotaquot-with-blue-marble-texture-suitable-design-branding-purposes_658005-53504.jpg?semt=ais_hybrid')



@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет!':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}{message.from_user.last_name}!')
    elif message.text.lower() == 'id' :
        bot.reply_to(message,f'ID: {message.from_user.id}')
    elif message.text.lower() == '/start':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}{message.from_user.last_name}!')

@bot.message_handler(commands=['start', 'help'])
def main (message):
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}{message.from_user.last_name}!')
    if message.text.lower() == 'мне плохо:(':
        bot.send_message(message.chat.id, f'{message.from_user.first_name} Расскажи быть может я смогу тебе помочь :)')




bot.polling(none_stop=True)


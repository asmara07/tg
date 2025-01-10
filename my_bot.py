import telebot
from telebot import types
import sqlite3

# --- Инициализация бота и базы данных ---
TOKEN = 'ВАШ_ТОКЕН'
bot = telebot.TeleBot(TOKEN)

# Подключение к базе данных
connection = sqlite3.connect('users.db', check_same_thread=False)
sql = connection.cursor()
sql.execute(" CREATE TABLE IF NOT EXISTS users"
            "( id INTEGER PRIMARY KEY AUTOINCREMENT",
        "user_id INTEGER UNIQUE,"
       " name TEXT, phone TEXT,language TEXT);")
connection.commit()

user_states = {}
@bot.message_handler(commands=['start'])
def start(message):
     user_id = message.from_user.id
     markup = types.InlineKeyboardMarkup()
     markup.add(
         types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_ru'),
         types.InlineKeyboardButton('🇺🇿 O‘zbekcha', callback_data='lang_uz'))
     bot.send_message(user_id, "👋 Привет! Выберите язык:", reply_markup=markup)

 @bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))][][0]

 def set_language(call):
     user_id = call.from_user.id
     language = 'ru' if call.data == 'lang_ru' else 'uz'

     user_states[user_id] = {'language': language}
     bot.send_message(user_id, "📝 Введите ваше имя:")

 @bot.message_handler(
     func=lambda message: message.chat.id in user_states and 'name' not in user_states[message.chat.id])
 def get_name(message):
     user_id = message.chat.id
     user_states[user_id]['name'] = message.text
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
     phone_button = types.KeyboardButton('📱 Отправить номер телефона', request_contact=True)
     markup.add(phone_button)
     bot.send_message(user_id, "📲 Отправьте свой номер телефона:", reply_markup=markup)


 @bot.message_handler(content_types=['contact'])
 def contact_handler(message):
     if message.contact:
         user_id = message.chat.id
         phone = message.contact.phone_number

         user_states[user_id]['phone'] = phone

         user_data = user_states[user_id]
         sql.execute('INSERT INTO users (user_id, name, phone, language) VALUES (?, ?, ?, ?)',
                     (user_id, user_data['name'], user_data['phone'], user_data['language']))
         connection.commit()

         bot.send_message(user_id, "✅ Регистрация завершена! Спасибо!")
         del user_states[user_id]

         bot.polling(none_stop=True)
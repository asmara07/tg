#1 бот конвертер валют

import telebot
import requests
bot = telebot.TeleBot("7732508153:AAE85TltOfQZJWUChVSn-2T9FiUPtflrS8M")

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url).json()
    rates = response["rates"]
    return rates
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Введите сумму в долларах, которую хотите конвертировать в евро, рубли и другие валюты:")
    bot.register_next_step_handler(message, convert_currency)
def convert_currency(message):
    try:
        amount = float(message.text)
        rates = get_exchange_rates()

        euros = round(amount * rates["EUR"], 2)
        rubles = round(amount * rates["RUB"], 2)

        bot.send_message(
            message.chat.id,
            f"{amount} USD равно:\n- {euros} EUR\n- {rubles} RUB")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
        bot.register_next_step_handler(message, convert_currency)

bot.polling()


#2 бот отвечающий за команду '/start`

import telebot
bot = telebot.TeleBot("7732508153:AAE85TltOfQZJWUChVSn-2T9FiUPtflrS8M")
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я ваш Telegram-бот. Чем могу помочь?")
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        message.chat.id,
        "Справочная информация:\n"
        "/start - Приветствие от бота\n"
        "/help - Показать справочную информацию")

bot.polling()

#3 свой Телеграмм-БОТ:

import telebot

bot = telebot.TeleBot("7732508153:AAE85TltOfQZJWUChVSn-2T9FiUPtflrS8M")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Как тебя зовут?")
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Приятно познакомиться, {name}! Отправь мне свой номер телефона.")
    request_phone(message)

def request_phone(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    phone_button = KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(phone_button)
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы отправить свой номер телефона.", reply_markup=keyboard)

@bot.message_handler(content_types=["contact"])
def get_phone(message):
    bot.send_message(message.chat.id, "Спасибо! Теперь отправь свою локацию.")
    request_location(message)

def request_location(message):
    keyboard = (ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True))
    location_button = (KeyboardButton(text="Отправить локацию", request_location=True))
    keyboard.add(location_button)
    bot.send_message(message.chat.id, "Нажми кнопку, чтобы отправить свою локацию.",
                     reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def get_location(message):
    bot.send_message(message.chat.id, "Регистрация завершена! Спасибо за предоставленные данные.")
bot.polling()





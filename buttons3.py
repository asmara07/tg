from telebot import types

def language_buttons():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_ru'))
    markup.add(types.InlineKeyboardButton('🇺🇿 Oʻzbekcha', callback_data='lang_uz'))
    return markup

def registration_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('📞 Отправить номер', request_contact=True))
    return markup

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('🛒 Корзина'))
    markup.add(types.KeyboardButton('💬 Оставить отзыв'))
    return markup

def cart_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('⬅️ Назад'))
    return markup
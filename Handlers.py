

from telebot.types import Message, CallbackQuery
from database3 import register_user, add_review, add_to_cart, get_cart
from buttons import language_buttons, registration_buttons, main_menu, cart_menu

def handle_language(bot, call: CallbackQuery):
    lang = call.data.split('_')[1]
    bot.send_message(call.message.chat.id, f'Язык выбран: {"Русский" if lang == "ru" else "Oʻzbekcha"}')
    bot.send_message(call.message.chat.id, '📞 Отправьте свой номер телефона для регистрации:', reply_markup=registration_buttons())
    bot.register_next_step_handler(call.message, handle_contact, bot, lang)

def handle_contact(message: Message, bot, lang):
    if message.contact:
        register_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.contact.phone_number, lang)
        bot.send_message(message.chat.id, '✅ Регистрация завершена!', reply_markup=main_menu())

def handle_review(message: Message, bot):
    review = message.text
    add_review(message.from_user.id, review)
    bot.send_message(message.chat.id, '✅ Спасибо за ваш отзыв!', reply_markup=main_menu())

def handle_cart(message: Message, bot):
    cart_items = get_cart(message.from_user.id)
    if cart_items:
        cart_text = '\n'.join([f'{item[0]} — {item[1]} шт.' for item in cart_items])
        bot.send_message(message.chat.id, f'🛒 Ваша корзина:\n{cart_text}', reply_markup=cart_menu())
    else:
        bot.send_message(message.chat.id, '🛒 Ваша корзина пуста.', reply_markup=cart_menu())
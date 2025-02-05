import telebot
from telebot import types

import os
from dotenv import load_dotenv

load_dotenv()

TK = os.getenv('tb')
bot = telebot.TeleBot(TK)
@bot.message_handler(commands=['start'])
def main(message):
    with open('./imagine/kk.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Наличие")
    button2 = types.KeyboardButton("Под заказ")
    button3 = types.KeyboardButton("Обо мне")
    button4 = types.KeyboardButton("Отзывы")
    keyboard.add(button1, button2, button3, button4)

    bot.send_message(message.chat.id,
                     'Доброго времени суток!\nЭтот бот поможет Вам ознакомиться с работами @vviral_l', reply_markup=keyboard)


photos = [
    ('./imagine/11.jpg', '450 ₽'),
    ('./imagine/2.jpg', '600 ₽'),
    ('./imagine/3.jpg', '999₽'),
    ('./imagine/4.jpg', '850 ₽'),
]

current_photo_index = 0



@bot.message_handler(func=lambda message: message.text == "Наличие")
def show_photos(message):
    global current_photo_index
    current_photo_index = 0
    send_photo_with_caption(message.chat.id, current_photo_index)


def send_photo_with_caption(chat_id, index):
    if index < 0 or index >= len(photos):
        return

    photo_path, caption = photos[index]

    try:
        with open(photo_path, 'rb') as photo_file:
            bot.send_photo(chat_id, photo_file, caption=caption)
    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка при отправке фото: {e}")


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if index < len(photos) - 1:
        keyboard.add(types.KeyboardButton("Вперед"))
    if index > 0:
        keyboard.add(types.KeyboardButton("Назад"))

    keyboard.add(types.KeyboardButton("Назад в меню"))

    bot.send_message(chat_id, 'Выберите действие:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == "Под заказ")
def show_order_info(message):
    bot.send_message(message.chat.id, 'Все ваши пожелания по заказу принимаю здесь: @vviral_l')

@bot.message_handler(func=lambda message: message.text == "Обо мне")
def show_join_staby(message):
    bot.send_message(message.chat.id, 'Доброго времени суток! Я Лиза18 и это мой тестовый мини-проект:)\nНадеюсь Вы поддержите его развитие и найдёте то, что будет Вам по душе!   ')


@bot.message_handler(func=lambda message: message.text == "Отзывы")
def show_facts(message):
    bot.send_message(message.chat.id, 'Раздел пока что на этапе разработки.\nСсылка на Авито: https://www.avito.ru/moskva/chasy_i_ukrasheniya/lovets_snov_brelok_4873802238?utm_campaign=native&utm_medium=item_page_ios&utm_source=soc_sharing_seller')


def send_photo_with_caption(chat_id, index):
    if index < 0 or index >= len(photos):
        return

    photo_path, caption = photos[index]

    with open('./imagine/1r.jpeg', 'rb') as photo_file:
        bot.send_photo(chat_id, photo_file, caption=caption)


@bot.message_handler(func=lambda message: message.text == "Наличие")
def show_photos(message):
    global current_photo_index
    current_photo_index = 0
    send_photo_with_caption(message.chat.id, current_photo_index)


def send_photo_with_caption(chat_id, index):
    if index < 0 or index >= len(photos):
        return

    photo_path, caption = photos[index]

    try:
        with open(photo_path, 'rb') as photo_file:
            bot.send_photo(chat_id, photo_file, caption=caption)
    except Exception as e:
        bot.send_message(chat_id, f"Произошла ошибка при отправке фото: {e}")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if index < len(photos) - 1:
        keyboard.add(types.KeyboardButton("Вперед"))
    if index > 0:
        keyboard.add(types.KeyboardButton("Назад"))
    keyboard.add(types.KeyboardButton("Назад в меню"))

    bot.send_message(chat_id, 'Выберите действие:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ["Вперед", "Назад"])
def change_photo(message):
    global current_photo_index

    if message.text == "Назад" and current_photo_index > 0:
        current_photo_index -= 1
    elif message.text == "Вперед" and current_photo_index < len(photos) - 1:
        current_photo_index += 1

    send_photo_with_caption(message.chat.id, current_photo_index)


@bot.message_handler(func=lambda message: message.text == "Назад в меню")
def back_to_menu(message):
    main(message)

bot.polling(none_stop=True)

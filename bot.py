import telebot
import films
from markup import *

TOKEN = '2067161053:AAFd1_GZJiWi3tkle28Ag_bkO7c1vEp8JL8'

bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print('INFO ~ ' + str(message.from_user.id) + ' = ' + message.from_user.first_name + ' - "' + message.text + '"')

    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDJZVhdmelY_UPvv1SCph9zeUcy8zrngACGgADHVUKFdBzSmAp7EJmIQQ')
    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}!☺️\nЯ - бот-портфолио замечательного поэта, актера, режиссера и гения Владимира Маяковского!\nПользуйся кнопками снизу.',
                     reply_markup=markup)


@bot.message_handler(content_types=['text', 'photo'])
def send_info(message):
    print('INFO ~ ' + str(message.from_user.id) + ' = ' + message.from_user.first_name + ' - "' + message.text + '"')

    if message.text == 'Биография🙎🏻‍♂️':
        photo = open('photos/bio.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        file = open('text/Биография.txt', 'r', encoding='utf-8')
        text = file.read()
        bot.send_message(message.chat.id, text, reply_markup=markup)
        file.close()

    elif message.text == 'Фильмы🎥':
        bot.send_message(message.chat.id, 'Выбери фильм:', reply_markup=markup_films)

    elif message.text == 'Фото📸':
        bot.send_message(message.chat.id, 'Выбери фото с помощью кнопок снизу 😏\nЕсли что список можно листать.', reply_markup=markup2)

    elif message.text == 'Детство' or message.text == 'Юность' or message.text == 'Молодость' or message.text == 'С Лилей Брик' or message.text == 'С Осипом' or message.text == 'Кольцо ЛЮБЛЮ' or message.text == 'Марка 1940' or message.text == 'Памятник в Москве' or message.text == 'С сигаркой' or message.text == 'С котиком' or message.text == 'Нордерне 1923' or message.text == 'Крым 1926':
        photo = open('photos/' + message.text + '.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()

        file = open('text/' + message.text + '.txt', 'r', encoding='utf-8')
        text = file.read()
        bot.send_message(message.chat.id, text, reply_markup=markup2)
        file.close()

    elif message.text == 'Вернуться назад':
        bot.send_message(message.chat.id, 'Возращаемся... 😊')
        bot.send_message(message.chat.id, 'Кнопки как всегда снизу.\nВыбери то что тебе нужно', reply_markup=markup)

    elif message.text == 'Стихотворения📝':
        bot.send_message(message.chat.id, 'Список можно листать.\nВыбери стихотворение:', reply_markup=markup_voice)

    elif message.text == 'Облако в штанах (отрывок)' or message.text == 'Вам' or message.text == 'Лиличка' or message.text == 'О советском паспорте' or message.text == 'Товарищу Нетте, параходу и человеку' or message.text == 'Тучкины штучки'or message.text == 'Хорошее отношение к лошадям' or message.text == 'Что такое хорошо и что такое плохо':
        m_id = bot.send_message(message.chat.id, 'Подождите немного...').message_id
        url_markup = types.InlineKeyboardMarkup()
        file_url = open('audio/text/' + message.text + '.txt', 'r')
        url_btn = types.InlineKeyboardButton(text='Читать!📖',
                                             url=file_url.read())
        file_url.close()
        url_markup.add(url_btn)
        audio = open('audio/voice/' + message.text + '.mp3', 'rb')
        bot.send_voice(message.chat.id, audio, reply_markup=url_markup)
        audio.close()
        bot.delete_message(message.chat.id, m_id)

    elif message.text == 'Сайт-Портфолио🌐':
        url_markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='Нажми!🕸️', url="https://alexshatokhin.github.io/VladimirMayakovsky/dist/")
        url_markup.add(url_btn)

        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEDTHhhk4xQNJ5qijQtCg7i2CyiITE1LgACzAQAAhyS0gMM4Xbjastl2iIE')
        bot.send_message(message.chat.id, 'Мой друг сделал сайт-портфолио Маяковского!\nОцени пожалуйста',
                         reply_markup=url_markup)

        back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn = types.KeyboardButton(text='Вернуться назад')
        back_markup.add(back_btn)
        bot.send_message(message.chat.id, 'Хотите вернуться назад?', reply_markup=back_markup)

    else:
        bot.send_message(message.chat.id, 'Я такое не понимаю, но мой разработчик уже работает, чтобы я понимал это!', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def send_next(call):
    if call.data == '0' or call.data == '1' or call.data == '2':
        photo = open('films/poster' + call.data + '.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo, reply_markup=markup)
        photo.close()

        url_markup = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='Смотреть фильм!🍿', url=films.film[int(call.data)]["link"])
        url_markup.add(url_btn)
        bot.send_message(call.message.chat.id,
                         f'<b>{films.film[int(call.data)]["name"]}</b>\nГод: <b><i>{films.film[int(call.data)]["year"]}</i></b>\nРейтинг: <b><i>{films.film[int(call.data)]["rating"]}</i></b> ⭐️\n{films.film[int(call.data)]["text"]}',
                         parse_mode='html', reply_markup=url_markup)

        back_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn = types.KeyboardButton(text='Вернуться назад')
        back_markup.add(back_btn)
        bot.send_message(call.message.chat.id, 'Хотите вернуться назад?', reply_markup=back_markup)

bot.infinity_polling()

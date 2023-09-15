from telebot import types


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Биография🙎🏻‍♂️')
item2 = types.KeyboardButton('Фильмы🎥')
item3 = types.KeyboardButton('Фото📸')
item4 = types.KeyboardButton('Стихотворения📝')
item5 = types.KeyboardButton('Сайт-Портфолио🌐')
markup.add(item1, item2, item3, item4, item5)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btns = [types.KeyboardButton(text='Детство'),
        types.KeyboardButton(text='Юность'),
        types.KeyboardButton(text='Молодость'),
        types.KeyboardButton(text='С Лилей Брик'),
        types.KeyboardButton(text='С Осипом'),
        types.KeyboardButton(text='Кольцо ЛЮБЛЮ'),
        types.KeyboardButton(text='С сигаркой'),
        types.KeyboardButton(text='С котиком'),
        types.KeyboardButton(text='Нордерне 1923'),
        types.KeyboardButton(text='Крым 1926'),
        types.KeyboardButton(text='Марка 1940'),
        types.KeyboardButton(text='Памятник в Москве'),
        types.KeyboardButton(text='Вернуться назад')]
for btn in btns:
    markup2.add(btn)

markup_voice = types.ReplyKeyboardMarkup(resize_keyboard=True)
btns_voice = [types.KeyboardButton(text='Облако в штанах (отрывок)'),
              types.KeyboardButton(text='Вам'),
              types.KeyboardButton(text='Лиличка'),
              types.KeyboardButton(text='О советском паспорте'),
              types.KeyboardButton(text='Товарищу Нетте, параходу и человеку'),
              types.KeyboardButton(text='Тучкины штучки'),
              types.KeyboardButton(text='Хорошее отношение к лошадям'),
              types.KeyboardButton(text='Что такое хорошо и что такое плохо'),
              types.KeyboardButton(text='Вернуться назад')
]
for btn in btns_voice:
    markup_voice.add(btn)

markup_films = types.InlineKeyboardMarkup()
film0 = types.InlineKeyboardButton(text='Закованная фильмой (1918)', callback_data='0')
film1 = types.InlineKeyboardButton(text='Барышня и хулиган (1918)', callback_data='1')
film2 = types.InlineKeyboardButton(text='Не для денег родившийся (1918)', callback_data='2')
markup_films.add(film0)
markup_films.add(film1)
markup_films.add(film2)


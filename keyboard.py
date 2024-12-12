from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton


greeting_button = KeyboardButton('Начать! 🔮')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(greeting_button)


aries_button = KeyboardButton('Овен ♈')
taurus_button = KeyboardButton('Телец ♉')
gemini_button = KeyboardButton('Близнецы ♊')
cancer_button = KeyboardButton('Рак ♋')

leo_button = KeyboardButton('Лев ♌')
virgo_button = KeyboardButton('Дева ♍')
libra_button = KeyboardButton('Весы ♎')
scorpio_button = KeyboardButton('Скорпион ♏')

sagittarius_button = KeyboardButton('Стрелец ♐')
capricorn_button = KeyboardButton('Козерог ♑')
aquarius_button = KeyboardButton('Водолей ♒')
pisces_button = KeyboardButton('Рыбы ♓')

markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(
    aries_button, taurus_button, gemini_button)
markup.row(cancer_button, leo_button, virgo_button)
markup.row(libra_button, scorpio_button, sagittarius_button)
markup.row(capricorn_button, aquarius_button, pisces_button)
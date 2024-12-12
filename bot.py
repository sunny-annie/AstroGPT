import random
import logging
import keyboard as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from config import TOKEN
from model import get_prediction

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="w")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

signs_dict = {"Овен ♈": "Овны",
              "Телец ♉": "Тельцы",
              "Близнецы ♊": "Близнецы",
              "Рак ♋": "Раки",
              "Лев ♌": "Львы",
              "Дева ♍": "Девы",
              "Весы ♎": "Весы",
              "Скорпион ♏": "Скорпионы",
              "Стрелец ♐": "Стрельцы",
              "Козерог ♑": "Козероги",
              "Водолей ♒": "Водолеи",
              "Рыбы ♓": "Рыбы"}

standby_messages_list = ["Одну минутку! Проверяем вашу натальную карту.",
                         "Сверяемся по звездам: придется немного подождать.",
                         "Звезды в процессе выравнивания. Вскоре ваше предсказание станет доступным.",
                         "Приготовьтесь! Ваш гороскоп в процессе создания.",
                         "Астрологический пазл собирается. Ваш гороскоп почти готов!",
                         "Ваш гороскоп кристаллизуется. Вскоре вы узнаете свою судьбу, предсказанную звездами!",
                         "Ваш гороскоп уже в пути, ожидайте!",
                         "Мы изучаем влияние планет на вашу судьбу. Ваш гороскоп будет готов в ближайшее время."]


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id} sent message: {message.text}')
    await message.reply(f'Привет, {user_name}! Я могу сгенерировать гороскоп для любого знака зодиака. '
                        'Нажми "Начать", чтобы приступить к генерации. \n'
                        '/help - вызвать помощь',
                        reply_markup=kb.greet_kb)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id} sent message: {message.text}')
    await message.reply("/start - запустить бота\n"
                        "/help - вызвать помощь\n"
                        "/select - выбрать знак зодиака\n")


@dp.message_handler(Text(equals="Начать! 🔮"))
@dp.message_handler(commands=['select'])
async def select_sign(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id} sent message: {message.text}')
    await message.reply("Выбери знак зодиака:", reply_markup=kb.markup)


@dp.message_handler(Text(equals=["Овен ♈", "Телец ♉", "Близнецы ♊",
                                 "Рак ♋", "Лев ♌", "Дева ♍",
                                 "Весы ♎", "Скорпион ♏", "Стрелец ♐",
                                 "Козерог ♑", "Водолей ♒", "Рыбы ♓"]))
async def generate_prediction(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    standby_reply = random.choice(standby_messages_list)
    await bot.send_message(message.from_user.id, standby_reply)
    logging.info(
        f'Message: "{standby_reply}" sent to user {user_name=} {user_id}')
    txt = get_prediction(signs_dict[message.text])
    logging.info(f'User {user_name=} {user_id} sent message: {message.text}. \n '
                 f'Message: "{txt}" sent to user {user_name=} {user_id}')
    await message.reply(txt, reply_markup=kb.markup)


@dp.message_handler()
async def process_random_messages(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name=} {user_id} sent message: {message.text}')
    await bot.send_message(message.from_user.id, f"{user_name}, выбери знак:", reply_markup=kb.markup)


if __name__ == '__main__':
    executor.start_polling(dp)

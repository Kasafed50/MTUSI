import random
import time
import telebot
from telebot import types

print("Link for BOT: t.me/MTUSI_FIRST_BOT")
f = open("dftg.lox")

token = f.read()
bot = telebot.TeleBot(token)


def game(message):
    time.sleep(1)
    bot.send_message(message.chat.id,
                     'Однако мы можем сыграть в пару игр. Так сказать ради сбора различных сведений о вас - млекопитающих 😊')
    time.sleep(0.2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Пожалуй можно")
    item2 = types.KeyboardButton("Только не с тобой!")
    keyboard.add(item1, item2)
    bot.send_message(message.chat.id, 'Согласен?', reply_markup=keyboard)


def game_challenge(message):
    time.sleep(0.2)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число 🎲")
    keyboard.add(item1)
    bot.send_message(message.chat.id, 'К сожалению пока я могу предложить тебе только это 😢', reply_markup=keyboard)


def andnow(message):
    time.sleep(1)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Начнем все с начала")
    item2 = types.KeyboardButton("INFO МТУСИ")
    item3 = types.KeyboardButton("Какой нынче курс валюты?")
    item4 = types.KeyboardButton("А почему так мало функций?")
    keyboard.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Ну? Чем займемся теперь?', reply_markup=keyboard)


def welcome(message):
    time.sleep(0.5)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Давай поговорим")
    item2 = types.KeyboardButton("А что ты можешь?")
    item3 = types.KeyboardButton("Дай мне больше кнопок")
    keyboard.add(item1, item2, item3)
    bot.send_message(message.chat.id, '???', reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    time.sleep(0.5)
    bot.send_message(message.chat.id, 'Приветствую!!!')

    time.sleep(1)
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    time.sleep(0.5)
    bot.send_message(message.chat.id, 'Чем обязан?')
    welcome(message)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')
    andnow(message)

@bot.message_handler(commands=['getmy'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')
    andnow(message)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "давай поговорим":
        time.sleep(1.5)
        bot.send_message(message.chat.id,
                         'Слушай, вот ты как считаешь, есть ли у меня на это время? Вас вобще-то много, а я один. '
                         'Пока вас всех обслужишь, состариться можно. Да ты верно не в себе.')
        game(message)

    elif message.text.lower() == "а что ты можешь?":
        time.sleep(1)
        bot.send_message(message.chat.id, 'Если тебе действительно интересно, то тебе сюда /help')

    elif message.text.lower() == "пожалуй можно":
        time.sleep(0.4)
        bot.send_message(message.chat.id, 'Во что хочешь поиграть?')
        game_challenge(message)

    elif message.text.lower() == "рандомное число 🎲":
        time.sleep(0.5)
        bot.send_message(message.chat.id, 'Я буду выбирать от 0 до 100')
        time.sleep(2)
        bot.send_message(message.chat.id, "Твое число " + str(random.randint(0, 100)))
        time.sleep(1)
        bot.send_message(message.chat.id, 'Хм... А это интересно 🤔')
        time.sleep(0.2)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Рандомное число 🎲")
        item2 = types.KeyboardButton("Хватит")
        keyboard.add(item1, item2)
        bot.send_message(message.chat.id, 'Может еще раз?', reply_markup=keyboard)

    elif message.text.lower() == "хватит":
        time.sleep(2)
        bot.send_message(message.chat.id, 'ой, какие мы суровые 😒')
        andnow(message)

    elif message.text.lower() == "дай мне больше кнопок":
        andnow(message)

    elif message.text.lower() == "начнем все с начала":
        welcome(message)

    elif message.text.lower() == "только не с тобой!":
        time.sleep(2)
        bot.send_message(message.chat.id, 'И как так можно?.. Я то с тобой по хорошему 😒')
        time.sleep(0.5)
        bot.send_message(message.chat.id, 'Ладно...')
        andnow(message)

    elif message.text.lower() == "а почему так мало функций?":
        time.sleep(1)
        bot.send_message(message.chat.id,
                         'Я хочу заметить, что я еще не столь развился, чтобы иметь огрмный функционал... \nБудтье впредь более солидарны к разработчику. Пожалуйста 😊')
        andnow(message)

    elif message.text.lower() == "info мтуси":
        time.sleep(1)
        bot.send_message(message.chat.id, 'Хм... Я думаю, что смогу тебе помочь с этим.')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Тут тебе точно помогут. И помогут лучше, чем я 🙃\nhttps://mtuci.ru/')
        andnow(message)

    elif message.text.lower() == "какой нынче курс валюты?":
        time.sleep(1)
        bot.send_message(message.chat.id, 'Ты шо? Ты здоров? Какой курс валюты? ')
        time.sleep(2)
        bot.send_message(message.chat.id,
                         'Вообщем у меня есть два пути, либо в дурку, либо ссылку. Что-ж, хорошо, я поверю в то, что ты испраишься и не будешь больше пугать меня такими вещами.')
        time.sleep(3)
        bot.send_message(message.chat.id,
                         'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B2%D0%B0%D0%BB%D1%8E%D1%82%D1%8B&aqs=chrome..69i57j0i457i512j0i512l8.8696j1j9&sourceid=chrome&ie=UTF-8')

    else:
        time.sleep(0.6)
        bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


bot.polling(none_stop=True)

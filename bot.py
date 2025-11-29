import telebot
from random import choice

from config import BOT_TOKEN
from weather import *
from lists import jokes, quotes, facts
from telebot import util
from car import *


bot = telebot.TeleBot(BOT_TOKEN) 

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    text = """
Привет! Я бот с различными командами:

/start или /help - это сообщение
/joke - случайная шутка
/quote - мудрая цитата
/fact - интересный факт
/weather - прогноз погоды
/coin - подбросить монетку
/car цвет марка [модель] - создать автомобиль

Пример: /car красный Toyota Camry
    """
    bot.reply_to(message, text)

@bot.message_handler(commands=['car'])
def car_handler(message):
    try:
        args_text = util.extract_arguments(message.text)
        
        if not args_text:
            bot.reply_to(message, "Неверно введена команда. Использование: /car цвет марка [модель]\nПример: /car синий BMW X5")
            return
        
        # Разбиваем аргументы на части
        args = args_text.split()
        
        if len(args) < 2:
            bot.reply_to(message, "Неверно введена команда. Нужно указать как минимум цвет и марку\nПример: /car черный Audi")
            return
        
        # Первый аргумент - цвет, второй - марка, остальные - модель
        color = args[0]
        brand = args[1]
        model = ' '.join(args[2:]) if len(args) > 2 else None
        
        # Создаем экземпляр автомобиля
        car = Car(color, brand, model)
        
        # Заводим двигатель и ускоряемся для демонстрации
        start_msg = car.start_engine()
        accelerate_msg = car.accelerate()
        
        # Формируем полное сообщение
        response = f"Автомобиль успешно создан!\n\n{car.info()}\n\n{start_msg}\n{accelerate_msg}"
        
        bot.reply_to(message, response)
        
    except Exception as e:
        bot.reply_to(message, f"❌ Произошла ошибка: {str(e)}")

@bot.message_handler(commands=['joke'])
def joke_handler(message):
    joke = choice(jokes)
    bot.reply_to(message, joke)

@bot.message_handler(commands=['quote'])
def quote_handler(message):
    quote = choice(quotes)
    bot.reply_to(message, quote)

@bot.message_handler(commands=['fact'])
def fact_handler(message):
    fact = choice(facts)
    bot.reply_to(message, fact)

@bot.message_handler(commands=['weather'])
def weather_handler(message):
    bot.reply_to(message, f'Погода: {weather}')
    bot.reply_to(message, f'Температура:  {temp}')


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
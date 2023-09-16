import webbrowser
import telebot
import requests
import json

bot = telebot.TeleBot('5953389314:AAFDuSpE488LpUC_bs7yfupwFt8BjOCFC9A')
API = 'f1d7a436cd2fab11eb4f5112ce1bd985'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@ bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:

        data = json.loads(res.text)
        bot.reply_to(message, f'Сейчас погода: {data["main"]["temp"]}')
    else:
        bot.reply_to(message, f'Город Указан не верно')

bot.polling(none_stop=True)
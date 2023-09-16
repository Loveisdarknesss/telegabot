
from aiogram import *
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5953389314:AAFDuSpE488LpUC_bs7yfupwFt8BjOCFC9A')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://gist.github.com/b62e8018ee3c43deec718fc7446051fa.git')))
    await message.answer('Привет, мой друг!', reply_markup= markup)

executor.start_polling(dp)



bot.polling(none_stop=True)
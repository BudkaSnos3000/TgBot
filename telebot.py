from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from urllib.request import quote

TOKEN = '5098301466:AAHGMkUOueH09eDvhbDuWKyhOg-QD6UyGgU'
bot = Bot(token=TOKEN)
languages = {
    'Английский': 'en',
    'Русский': 'ru'
}
dp = Dispatcher(bot)
text_users, text_translator = '', ''
url1, url2, endurl = 'https://translate.google.ru/?sl=ru&tl=en&text', '', '&op=translate'

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЭто бот переводчик, использующий переводчик от google")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(
        "Доступные комманды:"
        "\n/info - установленные параметры"
        "\n/change_lang1 - сменить язык переводимого сообщения"
        "\n/change_lang2 - сменить язык переведенного сообщения"
        "\n/switch - поменять местами языки ")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

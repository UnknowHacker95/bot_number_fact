import telebot
import requests
API_TOKEN = ''  # TODO: Вставьте сюда API_TOKEN вашего бота

START_STICKER = 'CAACAgIAAxkBAAEDU4NhmMgtcvAOws612v3FIqRQbAYnQgACKAADmWuhLSxox31sGp39IgQ'  # @Stiker_id_bot поможет
WIN_STICKER = 'CAACAgIAAxkBAAEDXxlhofzUZFEJyfjn7t2vosr1YR60tgACiwIAAladvQr3tGImDY878yIE'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, START_STICKER)
    bot.send_message(message.from_user.id, "Факты о числе. Отправь число")


@bot.message_handler(content_types=['text'])
def start(message):
    try:
        url = "http://numbersapi.com/" + message.text
        data = requests.get(url)
        bot.send_message(message.from_user.id, data.text)
        bot.send_sticker(message.chat.id, WIN_STICKER)
    except ValueError:
        bot.send_message(message.from_user.id, "Понимаю только целые числа")


@bot.message_handler(content_types=['voice'])
def start_message(message):
    bot.send_message(message.from_user.id, "Не слышуууу. Ничего не слышу. Глуховат я :(")


@bot.message_handler(content_types=['sticker'])
def start_message(message):
    bot.send_message(message.from_user.id, "Картинки какие-то шлют. Ничего не понимаю...")


@bot.message_handler(content_types=['document'])
def start_message(message):
    bot.send_message(message.from_user.id, "Ой, вот только файлы мне тут не надо слать!")


bot.polling()
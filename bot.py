import telebot
import time
import pyshorteners
import os

api = '2034893499:AAG-G8zrQpUTU4VbKAOToIheY7_6cQXbHD4'
bot = telebot.TeleBot(api)

def short(url):
    return pyshorteners.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hai, Selamat Datang di Bot Asistance Pearce, Gunakan Perintah di bawah untuk menjalakan bot nya.\n- /shortener Untuk merubah file menjadi link.')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, '- /shortener Untuk merubah file menjadi link.')

@bot.message_handler(commands=['shortener'], content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document[0].file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio[0].file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video[0].file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


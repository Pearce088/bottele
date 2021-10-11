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

@bot.message_handler(commands=['helpp'])
def send_welcome(message):
    bot.reply_to(message, '- /shortener Untuk merubah file menjadi link.')

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.reply_to(message, message.text)
    
@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
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
                
@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           'Message the developer', url='telegram.me/aanmhd08'
       )
   )
   bot.send_message(
       message.chat.id,
       '1) To receive a list of available currencies press /exchange.\n' +
       '2) Click on the currency you are interested in.\n' +
       '3) You will receive a message containing information regarding the source and the target currencies, ' +
       'buying rates and selling rates.\n' +
       '4) Click “Update” to receive the current information regarding the request. ' +
       'The bot will also show the difference between the previous and the current exchange rates.\n' +
       '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
       reply_markup=keyboard
   )


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


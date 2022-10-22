import sys
import time
import random
import datetime 
import telepot

def handle (msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == 'command1':
        bot.sendMessage(chat_id="925554964", text='Hello')
    elif command == 'command2':
        bot.sendMessage(chat_id="925554964", text='I am beautiful')
    elif command == 'photo':
        bot.sendPhoto(chat_id="925554964", photo=('https://cdn.pixabay.com/photo/2015/04/19/08/33/flower-729512__340.jpg'))

bot = telepot.Bot('5639985541:AAFl7ExhxXM3lYHMqiPSWNbDrm5OafSNKNQ')
bot.message_loop(handle)

while 1:
    time.sleep(10)


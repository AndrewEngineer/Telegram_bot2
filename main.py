# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#1774438370:AAEw2yqLuORgyEEbuqUswwiXicGkNy1JY6Y

import telebot
import time

token = '1774438370:AAEw2yqLuORgyEEbuqUswwiXicGkNy1JY6Y'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
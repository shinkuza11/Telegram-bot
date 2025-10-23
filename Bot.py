import telebot
import os

TOKEN = os.getenv("8256155430:AAF-bQpZk7EpBOOQfm1Ubv3h4Ab_lZIrJYQ")  # Bot-Token aus Umgebungsvariable
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hallo 👋 Ich bin online!")

print("Bot läuft...")
bot.infinity_polling()

import telebot
import os

# Lade den Bot-Token aus der Render-Umgebungsvariable
TOKEN = os.getenv("8256155430:AAF-bQpZk7EpBOOQfm1Ubv3h4Ab_lZIrJYQ")
bot = telebot.TeleBot(TOKEN)

# Wenn jemand /start schreibt
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "✅ Test vom Bot – ich bin online!")

print("🤖 Bot läuft ...")
bot.infinity_polling()

import telebot
import os

TOKEN = os.getenv("7823143146:AAGoasXtZY1H2-fDrrQUN-dEMW6xWcYqTeU")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def reply(message):
    if "سلام" in message.text:
        bot.reply_to(message, "سلام داداش 👋")
    elif "خوبی؟" in message.text:
        bot.reply_to(message, "خداروشکر 😎 تو چطوری؟")
    else:
        bot.reply_to(message, "هنوز یادم ندادی چی جواب بدم 😅")

bot.infinity_polling()

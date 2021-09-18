import telegram

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler
from app import translate

def start(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Welcome to our bot')


TOKEN = '1894855588:AAHDMz7xA1rMij6-fhOA4onudAghvYl5EKM'
updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text,translate))

# updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))


updater.start_polling()
updater.idle()
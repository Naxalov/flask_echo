from flask import Flask
from flask import request
import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler



app = Flask(__name__)
bot = telegram.Bot('1602686596:AAECWOgNbMCkfTUAxYEtKJFtnej6H6Dp5TA')

button1 = KeyboardButton(text = "Shahar yoki davlat nomini inglizchada yuboring")
button2 = KeyboardButton(text="Location yuboring", request_location = True)

buttons = ReplyKeyboardMarkup([[button1], [button2]], resize_keyboard=True)

def start(update, context):
    bot =context.bot
    update.message.reply_html(
        '<b>Assalomu alaykum, {}</b>\n \nMen namoz vaqtlari haqida ma`lumot beruvchi botman. Shahar nomini yuboring yoki Location yuboring'.format(update.message.from_user.first_name), reply_markup=buttons)
    return 1

def location_user(update, context):
    bot = context.bot
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    chat_id = update.message.from_user.id
    bot.sendMessage(chat_id, get_namoz_times(longitude, latitude))
    

def echo(update,context):
   bot = context.bot
   city_name = update.message.text
   text = get_by_city(city_name)
   chat_id = update.message.from_user.id
   bot.sendMessage(chat_id, text)
   print(city_name)


@app.route('/data',methods=['POST','GET'])
def get_data():
   if request.method=='POST':
      dp = Dispatcher(bot,None,workers=0)

      update = telegram.Update.de_json(request.json,bot)

      dp.add_handler(CommandHandler('start', start))
      dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
      dp.add_handler(MessageHandler(Filters.location, callback=location_user))

      dp.add_handler(MessageHandler(Filters.text,echo))
      dp.process_update(update)
      

   return {'error':0}

if __name__ == '__main__':
    app.run(debug=True)
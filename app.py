from flask import Flask
from flask import request
import telegram
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler


app = Flask(__name__)
bot = telegram.Bot('1602686596:AAECWOgNbMCkfTUAxYEtKJFtnej6H6Dp5TA')

def echo(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Welcome to our bot')

@app.route('/data',methods=['POST','GET'])
def get_data():
   if request.method=='POST':
      dp = Dispatcher(bot,None,workers=0)

      update = telegram.Update.de_json(request.json,bot)
      dp.add_handler(MessageHandler(Filters.text,echo))
      dp.process_update(update)
      # print(request.json)
      return {'result':0}
   return {'error':0}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import request
import telegram

app = Flask(__name__)
bot = telegram.Bot('1602686596:AAECWOgNbMCkfTUAxYEtKJFtnej6H6Dp5TA')
@app.route("/")
def get_sum():
   r = request.args
   a = int(r.get('a',0))
   b = int(r.get('b',0))
   
   return {'result':a+b} 

@app.route('/data',methods=['POST','GET'])
def get_data():
   if request.method=='POST':
      print(request.json)
      update = request.json['message']['text']
      chat_id = request.json['message']['from']['id']
      bot.sendMessage(chat_id,update)
      return {'result':0}
   return {'error':0}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import request
import telegram

app = Flask(__name__)
bot = telegram.Bot('1602686596:AAECWOgNbMCkfTUAxYEtKJFtnej6H6Dp5TA')

@app.route('/data',methods=['POST','GET'])
def get_data():
   if request.method=='POST':
      print(request.json)
      return {'result':0}
   return {'error':0}

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import request


app = Flask(__name__)

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
      return {'result':0}
   return {'error':0}

if __name__ == '__main__':
    app.run(debug=True)
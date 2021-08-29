from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def get_sum():
   r = request.args
   a = int(r.get('a',0))
   b = int(r.get('b',0))
   
   return {'result':a+b} 

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello():
   r = request.args
   data = int(r['a'])*2
   
   return str(data)

if __name__ == '__main__':
    app.run(debug=True)
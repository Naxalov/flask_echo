# Import Flask modules
from flask import Flask
# Create an object named app
app = Flask(__name__)
# Create a function named index which returns a string containing the text “Hello World!”
@app.route("/")
def index():
    return "Hello World!"

# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)

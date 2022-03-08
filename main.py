import os
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
   name = os.environ.get("NAME", "World")
   return "Hello {}!".format(name)


@app.route('/bot')
def show_bot():
   return render_template('bot.html')


if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
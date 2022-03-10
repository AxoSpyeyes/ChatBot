import os
from flask import *

from chatbothandler import answer
from imagehandler import choose_image
from info import update_info

app = Flask(__name__)
app.secret_key = ("aowdjajwdiwdjiajdsijdoiwa")
messages = []
image_history = [None]


@app.route('/')
def index():
   return 'hello world'


@app.route('/bot', methods=["GET"])
def show_bot():
   global image_history
   image_history = "./static/images/other/IKEA-opengraph.jpg"
   return render_template('bot.html', messages=messages, image=image_history)


@app.route('/send', methods=["GET", "POST"])
def send():
   if request.method == "POST":
      global image_history

      question = request.form.get("send-text")
# Returns answer from Bot
      response = answer(question)
# Chooses new random Image
      image = choose_image(response)
      response = image[1]
      image = image[0]

# Substitute info
      response = update_info(response)

# Update image history
      messages.append(["user", question])
      messages.append(["bot", response])
# Check if new image
      if image is not None:
         image_history = image
      else:
         image = image_history
      return render_template('bot.html', messages=messages, image=image)
   else:
      return render_template('bot.html')


if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
